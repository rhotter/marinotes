from flask import Flask, render_template, redirect, abort, request
from movement import getClasses, getInfo, getNotes, submitNote, rejectNote, acceptNote, uploadFile, deleteFile

application = Flask(__name__)

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
	uploadFile(file, path
	return "uploaded" # can render_template a page to go to

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = False
    application.run()
