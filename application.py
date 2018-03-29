from flask import Flask, render_template, redirect, abort
import csv

app = Flask(__name__)

classes = ['Calculus I', 'Calculus II', 'Calculus III', 'Linear Algebra', 'Mechanics', 'English']


@app.route("/")
def index():
	return render_template("index.html", classes=classes)

@app.route("/class/<course>")
def course(course):
	for c in classes:
		if c.replace(' ','') == course:
			# CSV stuff. Will need CSV files for each course

			# file = open("{}.csv".format(c),'r')
			# reader = csv.reader(file)
			
			# # CSV with rows as [teacher, author, upload date]
			# cards=[]
			# for row in reader:
			# 	cards.append(row)
			# file.close()
			return render_template("class.html", course=c)
	abort(404)


# @app.route("/", methods=["POST"])
# def register():

# @app.route("/zuck")
# def zuck():
# 	return render_template("zuck.html")

# request.form.get("name")
# import csv
# file = open(".csv","a")
# writer = csv.writer(file)
# writer.writerow((something,something,something))