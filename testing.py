from flask import Flask, render_template, redirect, abort
import os
import time

from flask_pymongo import PyMongo

application = Flask(__name__)
application.config['MONGO_DBNAME'] = 'server2'

with application.app_context():
    mongo = PyMongo(application)
    d = mongo.db.classes


# New functions (2)

def getClasses2():
    classes = []

    classes_curs = d.find({},{'name':1,'_id':0}).sort('name',1)
    for cl in classes_curs:
        classes.append(cl['name'])
    return classes

def getInfo2(course):
    teachers, students = [],[]

    info = d.find_one({'name':course},{'notes':1, '_id': 0})
    for inf in info['notes']:
        teachers.append(inf['teacher'])
        students.append(inf['student'])
    return teachers,students

def getNotes2(course,teacher,student):
    # Architechture here should be redone. Not optimal
    # for many notes in same class (which shouldn't be an issue)
    info = d.find({'name':course},{'_id':0,'notes':1})

    notes=[]
    for i in info[0]['notes']:
        if i['teacher']==teacher and i['student']==student:
            for j in i['files']:
                notes.append(j['name'][:-4])
            break;
    notes.sort()
    return notes


# Old functions (1)

def getClasses1():
	classes = next(os.walk('static/pdf/Notes'))[1]
	classes.sort()
	return classes

def getInfo1(course):
	teachers = []
	students = []
	for teacher in next(os.walk('static/pdf/Notes/%s' % course))[1]:
		for student in next(os.walk('static/pdf/Notes/%s/%s' % (course,teacher)))[1]:
			teachers.append(teacher)
			students.append(student)
	return teachers,students

def getNotes1(course,teacher,student):
	n = next(os.walk('static/pdf/Notes/%s/%s/%s/.' % (course,teacher,student)))[2]
	notes = []
	for note in n:
		if note[-4:]==".pdf":
			notes.append(note[:-4])
	notes.sort()
	return notes


course,teacher,student = 'Calculus 1 (Science)','Joseph Rinehart','Raffi Hotter'



time_start = time.clock()
notes = getNotes1(course,teacher,student)
print('getNotes (old)')
print(time.clock() - time_start)
print()

time_start = time.clock()
notes = getNotes2(course,teacher,student)
print('getNotes (new)')
print(time.clock() - time_start)
print()

time_start = time.clock()
notes = getInfo1(course)
print('getInfo (old)')
print(time.clock() - time_start)
print()

time_start = time.clock()
notes = getInfo2(course)
print('getInfo (new)')
print(time.clock() - time_start)
print()

time_start = time.clock()
notes = getClasses1()
print('getClasses (old)')
print(time.clock() - time_start)
print()

time_start = time.clock()
notes = getClasses2()
print('getClasses (new)')
print(time.clock() - time_start)
print()
