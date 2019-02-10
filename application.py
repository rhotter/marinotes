from flask import Flask, render_template, redirect, abort, request
from movement import getClasses, getInfo, getNotes, submitNote, rejectNote, acceptNote, uploadFile, deleteFile
from flask_pymongo import PyMongo
from config import S3_KEY, S3_SECRET, S3_BUCKET
import boto3

application = Flask(__name__)


"""
MongoDB functions
"""

application.config['MONGO_DBNAME'] = 'server2'

with application.app_context():
    mongo = PyMongo(application)
    d = mongo.db.classes

def getClasses():
    classes = []

    classes_curs = d.find({},{'name':1,'_id':0}).sort('name',1)
    for cl in classes_curs:
        classes.append(cl['name'])
    return classes

def getInfo(course):
    teachers, students = [],[]

    info = d.find_one({'name':course},{'notes':1, '_id': 0})
    for inf in info['notes']:
        print(inf)
        teachers.append(inf['teacher'])
        students.append(inf['student'])
    return teachers,students

def getNotes(course,teacher,student):
    # Architechture here should be redone. Not optimal
    # for many notes in same class (which shouldn't be an issue)
    info = d.find({'name':course},{'_id':0,'notes':1})

    notes=[]
    for i in info[0]['notes']:
        if i['teacher']==teacher and i['student']==student:
            for j in i['files']:
                notes.append(j['name'][:-4])
            break;
    notes.sort()
    return notes

"""
Amazon S3
"""
def uploadFile(file, path):
    s3_resource = boto3.resource('s3', aws_access_key_id=S3_KEY, aws_secret_access_key=S3_SECRET)
    my_bucket = s3_resource.Bucket(S3_BUCKET)
    my_bucket.Object(path).put(Body=file) # can put name of file here

def deleteFile(file):
	s3_resource = boto3.resource('s3', aws_access_key_id=S3_KEY, aws_secret_access_key=S3_SECRET)
	my_bucket = s3_resource.Bucket(S3_BUCKET)
	my_bucket.Object(file).delete()


"""
Different routes
"""
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
