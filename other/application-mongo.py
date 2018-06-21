from flask import Flask, render_template, redirect, abort
import os

from flask_pymongo import PyMongo

application = Flask(__name__)
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

@application.route("/")
def index():
	classes = getClasses()
	return render_template("index.html", classes=classes)

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


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = False
    application.run()
