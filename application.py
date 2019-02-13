from flask import Flask, render_template, redirect, abort, request, url_for
from movement import getClasses, getInfo, getNotes, submitNote, rejectNote, acceptNote, uploadFile, deleteFile
from flask_pymongo import PyMongo
from config import S3_KEY, S3_SECRET, S3_BUCKET
from werkzeug.utils import secure_filename
import boto3
from secret import MONGO_URI, bucket_name, user, AWS_SECRET_KEY, password
# from flask_login import LoginManager, login_required, UserMixin, login_user
from flask_basicauth import BasicAuth
from bson.objectid import ObjectId

application = Flask(__name__)

application.config['BASIC_AUTH_USERNAME'] = 'simon'
application.config['BASIC_AUTH_PASSWORD'] = password

basic_auth = BasicAuth(application)


"""
MongoDB
"""

application.secret_key = 'super secret key'
application.config["MONGO_URI"] = MONGO_URI

with application.app_context():
    mongo = PyMongo(application)
    d = mongo.db.classes

def name_to_id(class_name):
    return class_name.replace(' ', '+')

def id_to_name(class_id):
    return class_id.replace('+', ' ')

def approve(author_id, course_name, teacher_name, author_name, date, email, file_names):
    author = d.find_one({'_id': ObjectId(author_id)})
    teacher = d.find_one({'_id': author['parent']})
    course = d.find_one({'_id': teacher['parent']})
    for i, file_id in enumerate(author['children']):
        d.update_one({'_id': file_id}, # update files
                     {'$set':
                         {'name': file_names[i],
                          'approved': True}})
    d.update_one({'_id': author['_id']}, # update author
                 {'$set':
                     {'name': author_name,
                      'email': email,
                      'date': date,
                      'approved': True}})
    d.update_one({'_id': teacher['_id']}, # update teacher
                 {'$set':
                     {'name': teacher_name,
                      'approved': True}})
    d.update_one({'_id': course['_id']}, # update course
                 {'$set':
                     {'name': course_name,
                      'approved': True}})

def upload_notes(class_name, teacher, author, date, file_names, email, approved=False):
    if not d.find_one({'_id': 'classes'}):
        d.insert({'_id': 'classes', 'children': []})

    # Figure out how much has already been stored
    class_info = d.find_one({'_id': name_to_id(class_name)})
    teacher_info = None
    existing_teacher = True
    if class_info:
        existing_class = True
        teacher_id_array = [{'_id': teacher_id} for teacher_id in class_info['children']]
        # if teacher_id_array:
        #     teacher_info = d.find_one({'$or': teacher_id_array})
    else:
        class_info_id = d.insert({'type': 'class',
                               'name': class_name,
                               'children': [],
                               'parent': 'classes',
                               'approved': approved })
        class_info = d.find_one({'_id': class_info_id})
        class_list = d.find_one({'_id': 'classes'})
        class_list['children'].append(class_info['_id'])
        d.update_one({'_id': 'classes'},
                     {'$set':
                         {'children':
                             class_list['children']}})
    if not teacher_info:
        existing_teacher = False
        teacher_info_id = d.insert({'type': 'teacher',
                                 'name': teacher,
                                 'children': [],
                                 'parent': class_info['_id'],
                                 'approved': approved })
        teacher_info = d.find_one({'_id': teacher_info_id})

    author_info_id = d.insert({'type': 'author',
                            'name': author,
                            'date': date,
                            'children': [],
                            'email': email,
                            'parent': teacher_info['_id'],
                            'approved': approved })
    author_info = d.find_one({'_id': author_info_id})
    file_ids = []
    base_url = '{}/{}/{}/'.format(name_to_id(class_name), name_to_id(teacher),
                                  name_to_id(author))
    for file_name in file_names:
        file_ids.append(d.insert({'url': base_url + file_name,
                                  'type': 'note',
                                  'name': file_name,
                                  'parent': author_info['_id'],
                                  'approved': approved}))
    # propagate back up to update children
    d.update_one({'_id': author_info['_id']},
                 {'$set':
                    {'children': file_ids}
                 })

    teacher_info['children'].append(author_info['_id'])
    d.update_one({'_id': teacher_info['_id']},
              {'$set':
                 {'children':
                     teacher_info['children']}
              })
    if not existing_teacher:
        d.update_one({'_id': class_info['_id']},
                {'$set':
                   {'children':
                       class_info['children'].append(teacher_info['_id'])}
                })

# upload_notes('Calculus 3 (Science)', 'Joseph Rinehart', 'Raffi Hotter', 'March 3, 2018', ['Notes_1.pdf', 'Notes_2.pdf'])

"""
AWS S3
"""

def upload_file(file, path):
    s3_resource = boto3.resource('s3', aws_access_key_id=user, aws_secret_access_key=AWS_SECRET_KEY)
    my_bucket = s3_resource.Bucket(bucket_name)
    my_bucket.Object(path).put(Body=file, ContentType='application/pdf') # can put name of file here

def delete_file(file):
	s3_resource = boto3.resource('s3', aws_access_key_id=S3_KEY, aws_secret_access_key=S3_SECRET)
	my_bucket = s3_resource.Bucket(S3_BUCKET)
	my_bucket.Object(file).delete()

"""
Different routes
"""
@application.route("/upload-test")
def upload_test():
    return render_template('upload_test.html')

@application.route("/upload-test-post", methods=["POST"])
def upload_test_post():
    files = request.files.getlist('file')
    class_name = request.form['course']
    teacher = request.form['teacher']
    author = request.form['author']
    email = 'sample@gmail.com'
    date = ''
    base_url = 'Notes/marinotes-pdfs/{}/{}/{}/'.format(class_name, teacher, author)
    file_names = []
    for file in files:
        file.filename = secure_filename(file.filename)
        file_names.append(file.filename)
        url = base_url + file.filename
        upload_file(file, url)
    upload_notes(class_name, teacher, author, date, file_names, email,
                 approved=False)
    return 'uploaded'

@application.route("/admin-post", methods=["POST"])
def admin_post():
    checked_ids = request.form.getlist('checkbox')
    for id in checked_ids:
        course = request.form['course-{}'.format(id)]
        teacher = request.form['teacher-{}'.format(id)]
        author = request.form['author-{}'.format(id)]
        date = request.form['date-{}'.format(id)]
        email = request.form['email-{}'.format(id)]
        files = request.form.getlist('file-{}'.format(id))
        approve(id, course, teacher, author, date, email, files)
    return redirect(url_for('admin'))

@application.route("/admin")
@basic_auth.required
def admin():
    submissions = []
    notes = d.find({'type': 'author', 'approved': False})
    for author in notes:
        teacher = d.find_one({'_id': author['parent']})
        course = d.find_one({'_id': teacher['parent']})
        files = [d.find_one({'_id': file}) for file in author['children']]
        date = author['date']
        email = author['email']
        submissions.append({'id': author['_id'],
                            'course': course['name'],
                            'teacher': teacher['name'],
                            'author': author['name'],
                            'date': date,
                            'email': email,
                            'files': files})
    return render_template("admin.html", submissions=submissions)

@application.route("/")
def index():
	classes = getClasses()
	return render_template("index.html", classes=classes)

@application.route("/share")
def share():
	return render_template("share.html")

@application.route("/share-form")
def shareForm():
	return render_template("share-form.html")

@application.route("/class/<course>")
def note(course):
	classes = getClasses()
	for c_spaces in classes:
		c=c_spaces.replace(' ','')
		if c == course:
			teachers,students = getInfo(c_spaces)
			return render_template("class.html", course=c_spaces, teachers=teachers, students=students)
	abort(404)

@application.route("/note/<string>")
def teach(string):
	s = string.split('+')
	# check if input is good
	if len(s) != 3:
		abort(404)
	classes = getClasses()
	for c in classes:
		c_cut = c.replace(' ','')
		if c_cut==s[0]:
			teachers,students = getInfo(c)
			for t in teachers:
				if t.replace(' ','')==s[1]:
					for st in students:
						if st.replace(' ','')==s[2]:
								notes = getNotes(c,t,st)
								return render_template("note.html", course=c,teacher=t,student=st,notes=notes)
	abort(404)

@application.route('/upload', methods=['POST'])
def upload():
	file = request.files['file']
	folder = request.form.get('folder')
	name = request.form.get('name')
	path = folder + name
	uploadFile(file, path)
	return 'uploaded' # can render_template a page to go to

@application.route('/edit', methods=['GET'])
def edit():
	return render_template("edit.html")

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = False
    application.run()


    # submissions = [{'course': 'Linear Algebra',
    #                 'teacher': 'Riccardo Catalano',
    #                 'author': 'Raffi Hotter',
    #                 'date': 'March 1, 2018',
    #                 'files': ['Notes-1.pdf', 'Notes-2.pdf']},
    #                {'course': 'Linear Algebra',
    #                 'teacher': 'Riccardo Catalano',
    #                 'author': 'Raffi Hotter',
    #                 'date': 'March 1, 2018',
    #                 'files': ['Notes-1.pdf', 'Notes-2.pdf']}
    #                 ]

# @application.route("/login", methods=["GET", "POST"])
# def login():
#     error=None
#     if request.method == "POST":
#         if request.form['password'] == password:
#             user = User(1)
#             login_user(user)
#             return redirect(url_for('admin'))
#         else:
#             error = "Incorrect password"
#     return render_template("admin-login.html", error=error)
