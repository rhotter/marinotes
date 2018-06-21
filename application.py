from flask import Flask, render_template, redirect, abort
import os, sqlite3

application = Flask(__name__)

def getClasses():
	conn = sqlite3.connect('database.db')
	c = conn.cursor()

	c.execute("SELECT courseName FROM courses ORDER BY courseName;")
	classes = c.fetchall()
	return [x[0] for x in classes]

	conn.commit()
	conn.close()

def getInfo(course):
	conn = sqlite3.connect('database.db')
	c = conn.cursor()

	c.execute("SELECT studentName, teacherName FROM notes JOIN courses ON notes.courseID = courses.courseID JOIN students ON notes.studentID = students.studentID JOIN teachers ON notes.teacherID=teachers.teacherID WHERE courseName=?",(course,))
	teachstude = c.fetchall()
	return [x[1] for x in teachstude],[x[0] for x in teachstude] # teachers,students

	conn.commit()
	conn.close()

def getNotes(course,teacher,student):
	conn = sqlite3.connect('database.db')
	c = conn.cursor()

	c.execute("SELECT fileName FROM notes JOIN courses ON notes.courseID = courses.courseID JOIN students ON notes.studentID = students.studentID JOIN teachers ON notes.teacherID=teachers.teacherID JOIN files ON notes.noteID=files.noteID WHERE courseName=? AND teacherName=? AND studentName=? ORDER BY fileName",(course,teacher,student,))
	files = c.fetchall()
	print(files)
	return [x[0][:-4] for x in files] # remove ".PDF" from name

	conn.commit()
	conn.close()

def submitNote(course, teacher, student, date):

def acceptNote(submittedNoteID):
	conn = sqlite3.connect('database.db')
	c = conn.cursor()

	# (1) Get info from submittedNoteID
	c.execute("SELECT submittedCourse submittedTeacher submittedStudent submittedDate from submittedNotes WHERE submittedNoteId=?;",(submittedNoteID,))
	info = c.fetchone()
	info = info[0]
	course,teacher,student,date = info[0],info[1],info[2],info[3]

	c.execute("SELECT submittedFileName path FROM submittedFiles WHERE submittedNoteID=?",(submittedNoteID,))
	submittedFiles = c.fetchall()


	# (2) Check if student, teacher, course exists; if not, create one
	c.execute("SELECT studentID FROM students WHERE studentName=?;",(student,))
	studentID = c.fetchone()
	if studentID = None:
		c.execute("INSERT INTO students (studentName) VALUES (?);",(student,))
		c.execute("SELECT studentID FROM students WHERE studentName=?;",(student,))
		studentID = c.fetchone()
	studentID = studentID[0]

	c.execute("SELECT teacherID FROM teachers WHERE teacherName=?;",(teacher,))
	teacherID = c.fetchone()
	if teacherID = None:
		c.execute("INSERT INTO teachers (teacherName) VALUES (?);",(teacher,))
		c.execute("SELECT teacherID FROM teachers WHERE teacherName=?;",(teacher,))
		teacherID = c.fetchone()
	teacherID = teacherID[0]

	c.execute("SELECT courseID FROM coureses WHERE courseName=?;",(course,))
	courseID = c.fetchone()
	if courseID = None:
		c.execute("INSERT INTO courses (courseName) VALUES (?);",(course,))
		c.execute("SELECT courseID from coureses WHERE courseName=?;",(course,))
		courseID = c.fetchone()
	courseID = courseID[0]

	# (3) Add note to notes, file to files
	c.execute("INSERT INTO notes (courseID,teacherID,studentID,date) VALUES (?,?,?,?);",(courseID,teacherID,studentID,date))
	c.execute("SELECT noteID FROM notes WHERE courseID=? AND teacherID=? AND studentID=? AND date=?;",(courseID,teacherID,studentID,date))
	noteID = c.fetchall()
	if noteID.length > 1:
		return -1 # If note with these names already exist
	noteID = noteID[0]

	for fileName in submittedFileNames:
		c.execute("INSERT INTO files (noteID,fileName,date) VALUES (?,?,?);",(noteID,fileName,date))

	# (4) Delete the stuff
	c.execute("DELETE FROM submittedNotes WHERE submittedNoteID=?",(submittedNoteID,))
	c.execute("DELETE FROM submittedFiles WHERE submittedNoteID=?",(submittedNoteID,))

	# Also need to delete the stuff from the database

	conn.commit()
	conn.close()

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
