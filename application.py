from flask import Flask, render_template, redirect, abort
import csv
import os

application = Flask(__name__)

# classes = ['Calculus I', 'Calculus II', 'Calculus III', 'Linear Algebra', 'Mechanics', 'English']
#
# def getClasses():
# 	file = open("static/csv/classes.csv",'r', encoding='utf-8-sig') # Class CSV is classes.csv
# 	reader = csv.reader(file)
# 	# CSV with rows as [teacher, author, upload date]
# 	classes=[]
# 	for row in reader:
# 		classes.append(row[0])
# 	file.close()
#
# 	classes=sorted(classes[1:])
#
# 	return classes

def getClasses():
	return next(os.walk('static/pdf/Notes'))[1]

def getInfo(course):
	teachers = []
	students = []
	for teacher in next(os.walk('static/pdf/Notes/%s' % course))[1]:
		for student in next(os.walk('static/pdf/Notes/%s/%s' % (course,teacher)))[1]:
			teachers.append(teacher)
			students.append(student)
	return teachers,students

def getNotes(course,teacher,student):
	notes = next(os.walk('static/pdf/Notes/%s/%s/%s/.' % (course,teacher,student)))[2]
	for i in range(0,len(notes)):
		notes[i] = notes[i][:-4]
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

			# # CSV stuff. Will need CSV files for each course
			# file = open("static/csv/{}.csv".format(c),'r', encoding='utf-8-sig')
			# reader = csv.reader(file)
			#
			# # CSV with rows as [teacher, author, upload date]
			# cards=[]
			# for row in reader:
			# 	cards.append(row)
			# file.close()
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
								# notes = getNotes(string) # downloadable notes
								return render_template("note.html", course=c,teacher=t,student=st,notes=notes)
	abort(404)


# @application.route("/share")
# def share():
# 	return render_template("share.html")
# 	# http://127.0.0.1:5000/note/English+AndrewMcCambridge+QinyuCiu

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
