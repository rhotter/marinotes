import sqlite3, boto3
from config import S3_KEY, S3_SECRET, S3_BUCKET

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

def submitNote(submittedCourse, submittedTeacher, submittedStudent, submittedDate, Files_Paths):
	# Files_Paths is a list of tuples with file names and paths
	conn = sqlite3.connect('database.db')
	c = conn.cursor()

	c.execute("SELECT studentID FROM students WHERE studentName=?;",(student,))

	c.execute("INSERT INTO submittedNotes (submittedCourse,submittedTeacher,submittedStudent,submittedDate) VALUES (?,?,?,?);",(submittedCourse, submittedTeacher, submittedStudent, submittedDate))
	c.execute("SELECT submittedNoteID from submittedNotes WHERE submittedCourse=? AND submittedTeacher=? AND submittedStudent=? AND submittedDate=?;",(submittedCourse, submittedTeacher, submittedStudent, submittedDate))
	submittedNoteID = c.fetchone()
	submittedNoteID = submittedNoteID[0]

	for file_path in Files_Paths:
		c.execute("INSERT INTO submittedFiles (submittedNoteID, submittedFileName, path) VALUES (?,?,?);",(submittedNoteID, file_path[0], file_path[1]))

	conn.commit()
	conn.close()

def rejectNote(submittedNoteID):
	conn = sqlite3.connect('database.db')
	c = conn.cursor()

	c.execute("DELETE FROM submittedNotes WHERE submittedNoteID=?",(submittedNoteID,))
	c.execute("DELETE FROM submittedFiles WHERE submittedNoteID=?",(submittedNoteID,))

	conn.commit()
	conn.close()

def acceptNote(submittedNoteID):
	conn = sqlite3.connect('database.db')
	c = conn.cursor()

	# (1) Get info from submittedNoteID
	c.execute("SELECT submittedCourse, submittedTeacher, submittedStudent, submittedDate FROM submittedNotes WHERE submittedNoteId=?;",(submittedNoteID,))
	info = c.fetchone()
	info = info[0]
	course,teacher,student,date = info[0],info[1],info[2],info[3]

	c.execute("SELECT submittedFileName, path FROM submittedFiles WHERE submittedNoteID=?",(submittedNoteID,))
	submittedFiles = c.fetchall()

	# (2) Check if student, teacher, course exists; if not, create one
	c.execute("SELECT studentID FROM students WHERE studentName=?;",(student,))
	studentID = c.fetchone()
	if studentID == None:
		c.execute("INSERT INTO students (studentName) VALUES (?);",(student,))
		c.execute("SELECT studentID FROM students WHERE studentName=?;",(student,))
		studentID = c.fetchone()
	studentID = studentID[0]

	c.execute("SELECT teacherID FROM teachers WHERE teacherName=?;",(teacher,))
	teacherID = c.fetchone()
	if teacherID == None:
		c.execute("INSERT INTO teachers (teacherName) VALUES (?);",(teacher,))
		c.execute("SELECT teacherID FROM teachers WHERE teacherName=?;",(teacher,))
		teacherID = c.fetchone()
	teacherID = teacherID[0]

	c.execute("SELECT courseID FROM courses WHERE courseName=?;",(course,))
	courseID = c.fetchone()
	if courseID == None:
		c.execute("INSERT INTO courses (courseName) VALUES (?);",(course,))
		c.execute("SELECT courseID FROM courses WHERE courseName=?;",(course,))
		courseID = c.fetchone()
	courseID = courseID[0]

	# (3) Add note to notes, file to files
	c.execute("INSERT INTO notes (courseID,teacherID,studentID,date) VALUES (?,?,?,?);",(courseID,teacherID,studentID,date))
	c.execute("SELECT noteID FROM notes WHERE courseID=? AND teacherID=? AND studentID=? AND date=?;",(courseID,teacherID,studentID,date))
	noteID = c.fetchall()
	if len(noteID) > 1:
		return -1 # If note with these names already exist
	noteID = noteID[0][0]

	print(submittedFiles)
	for fileName in submittedFiles:
		c.execute("INSERT INTO files (noteID,fileName,path) VALUES (?,?,?);",(noteID,fileName[0],fileName[1]))

	# (4) Delete the stuff
	c.execute("DELETE FROM submittedNotes WHERE submittedNoteID=?",(submittedNoteID,))
	c.execute("DELETE FROM submittedFiles WHERE submittedNoteID=?",(submittedNoteID,))

	# Also need to delete the stuff from the database

	conn.commit()
	conn.close()

def uploadFile(file, path):
    s3_resource = boto3.resource('s3', aws_access_key_id=S3_KEY, aws_secret_access_key=S3_SECRET)
    my_bucket = s3_resource.Bucket(S3_BUCKET)
    my_bucket.Object(path).put(Body=file) # can put name of file here

def deleteFile(file):
	s3_resource = boto3.resource('s3', aws_access_key_id=S3_KEY, aws_secret_access_key=S3_SECRET)
	my_bucket = s3_resource.Bucket(S3_BUCKET)
	my_bucket.Object(file).delete()
