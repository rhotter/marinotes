from flask import Flask, render_template, redirect, abort
import os, sqlite3

conn = sqlite3.connect('database-upd3.db')
c = conn.cursor()

application = Flask(__name__)

def getClasses():
	c.execute("SELECT courseName FROM courses ORDER BY courseName;")
	classes = c.fetchall()
	return [x[0] for x in classes]

def getInfo(course):
	c.execute("SELECT studentName, teacherName from notes JOIN courses ON notes.courseID = courses.courseID JOIN students ON notes.studentID = students.studentID JOIN teachers ON notes.teacherID=teachers.teacherID WHERE courseName=?",(course,))
	teachstude = c.fetchall()
	return [x[1] for x in teachstude],[x[0] for x in teachstude] # teachers,students

def getNotes(course,teacher,student):
	c.execute("SELECT fileName from notes JOIN courses ON notes.courseID = courses.courseID JOIN students ON notes.studentID = students.studentID JOIN teachers ON notes.teacherID=teachers.teacherID JOIN files ON notes.noteID=files.noteID WHERE courseName=? AND teacherName=? AND studentName=? ORDER BY fileName",(course,teacher,student,))
	files = c.fetchall()
	print(files)
	return [x[0][:-4] for x in files]

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
