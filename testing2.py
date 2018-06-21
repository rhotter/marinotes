import os,time,sqlite3

conn = sqlite3.connect('database-upd3.db')
c = conn.cursor()

def getClasses1():
	c.execute("SELECT courseName FROM courses ORDER BY courseName;")
	classes = c.fetchall()
	return [x[0] for x in classes]

def getInfo1(course):
	c.execute("SELECT studentName, teacherName from notes JOIN courses ON notes.courseID = courses.courseID JOIN students ON notes.studentID = students.studentID JOIN teachers ON notes.teacherID=teachers.teacherID WHERE courseName=?",(course,))
	teachstude = c.fetchall()
	return [x[1] for x in teachstude],[x[0] for x in teachstude] # teachers,students

def getNotes1(course,teacher,student):
    c.execute("SELECT fileName from notes JOIN courses ON notes.courseID = courses.courseID JOIN students ON notes.studentID = students.studentID JOIN teachers ON notes.teacherID=teachers.teacherID JOIN files ON notes.noteID=files.noteID WHERE courseName=? AND teacherName=? AND studentName=?",(course,teacher,student,))
    files = c.fetchall()
    files = [x[0][:-4] for x in files]
    return files.sort()

def getClasses2():
	classes = next(os.walk('static/pdf/Notes'))[1]
	classes.sort()
	return classes

def getInfo2(course):
	teachers = []
	students = []
	for teacher in next(os.walk('static/pdf/Notes/%s' % course))[1]:
		for student in next(os.walk('static/pdf/Notes/%s/%s' % (course,teacher)))[1]:
			teachers.append(teacher)
			students.append(student)
	print(teachers,students)
	return teachers,students

def getNotes2(course,teacher,student):
	n = next(os.walk('static/pdf/Notes/%s/%s/%s/.' % (course,teacher,student)))[2]
	notes = []
	for note in n:
		if note[-4:]==".pdf":
			notes.append(note[:-4])
	notes.sort()
	return notes

course,teacher,student = 'Capitalism vs Environmentalism','Hugo Hamel-Perron','Maxine Steuer'

time_start = time.clock()
notes = getNotes1(course,teacher,student)
print('getNotes1')
print(time.clock() - time_start)
print()

time_start = time.clock()
notes = getNotes2(course,teacher,student)
print('getNotes2')
print(time.clock() - time_start)
print()

time_start = time.clock()
notes = getClasses1()
print('getClasses1')
print(time.clock() - time_start)
print()

time_start = time.clock()
notes = getClasses2()
print('getClasses2')
print(time.clock() - time_start)
print()

time_start = time.clock()
notes = getInfo2(course)
print('getInfo1')
print(time.clock() - time_start)
print()

time_start = time.clock()
notes = getInfo2(course)
print('getInfo2')
print(time.clock() - time_start)
print()

# 0.0008599999999999997
