from flask import Flask, render_template, redirect, abort
import csv
import os

application = Flask(__name__)

def getClasses():
	classes = next(os.walk('static/pdf/Notes'))[1]
	classes.sort()
	return classes

def getInfo(course):
	teachers = []
	students = []
	for teacher in next(os.walk('static/pdf/Notes/%s' % course))[1]:
		for student in next(os.walk('static/pdf/Notes/%s/%s' % (course,teacher)))[1]:
			teachers.append(teacher)
			students.append(student)
	return teachers,students

def getNotes(course,teacher,student):
	n = next(os.walk('static/pdf/Notes/%s/%s/%s/.' % (course,teacher,student)))[2]
	notes = []
	for note in n:
		if note[-4:]==".pdf":
			notes.append(note[:-4])
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
