from flask import Flask, render_template, redirect, abort
import csv

application = Flask(__name__)

# classes = ['Calculus I', 'Calculus II', 'Calculus III', 'Linear Algebra', 'Mechanics', 'English']

def getClasses():
	file = open("static/csv/classes.csv",'r', encoding='utf-8-sig') # Class CSV is classes.csv
	reader = csv.reader(file)
	# CSV with rows as [teacher, author, upload date]
	classes=[]
	for row in reader:
		classes.append(row[0])
	file.close()

	classes=sorted(classes[1:])

	return classes

def getInfo(course):
	course = course.replace(' ','')
	file = open("static/csv/%s.csv" % course,'r', encoding='utf-8-sig')
	reader = csv.reader(file)

	teachers=[]
	students=[]

	for row in reader:
		teachers.append(row[0])
		students.append(row[1])
	file.close()

	return teachers,students

def getNotes(string):
	file = open("static/csv/%s.csv" % string,'r', encoding='utf-8-sig')
	reader = csv.reader(file)

	notes = []

	for row in reader:
		notes.append(row[0])
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
			# CSV stuff. Will need CSV files for each course
			file = open("static/csv/{}.csv".format(c),'r', encoding='utf-8-sig')
			reader = csv.reader(file)

			# CSV with rows as [teacher, author, upload date]
			cards=[]
			for row in reader:
				cards.append(row)
			file.close()
			return render_template("class.html", course=c_spaces, cards=cards)
	abort(404)

@application.route("/note/<string>")

def teach(string):
	s = string.split('+')
	# check if input is good
	if len(s) != 3:
		abort(404)
	classes = getClasses()

	teachers,students = getInfo(s[0])

	for c in classes:
		if c.replace(' ','')==s[0]:
			for t in teachers:
				if t.replace(' ','')==s[1]:
					for st in students:
						if st.replace(' ','')==s[2]:
								notes = getNotes(string) # downloadable notes
								return render_template("note.html", course=c,teacher=t,student=st,notes=notes)
	abort(404)

#
# @application.route("/share")
# def share():
# 	return render_template("share.html")
# 	# http://127.0.0.1:5000/note/English+AndrewMcCambridge+QinyuCiu
