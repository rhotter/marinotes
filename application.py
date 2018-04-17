from flask import Flask, render_template, redirect, abort
import csv

app = Flask(__name__)

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

@app.route("/")
def index():
	classes = getClasses()
	return render_template("index.html", classes=classes)

@app.route("/class/<course>")
def course(course):
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

@app.route("/share")
def share():
	return render_template("share.html")

@app.route("/example")
def example():
	return render_template("note.html", course='Calculus')