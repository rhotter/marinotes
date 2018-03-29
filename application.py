from flask import Flask, render_template

app = Flask(__name__)

classes = ['Calculus I', 'Calculus II', 'Calculus III', 'Linear Algebra', 'Mechanics', 'English']

@app.route("/")
def index():
	return render_template("index.html", classes=classes)

@app.route("/%s" % (classes[0].replace(' ','')))
def cal():
	return render_template("class.html")


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