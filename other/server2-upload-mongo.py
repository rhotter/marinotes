# Put data from folders into MongoDB database

from flask import Flask, render_template, redirect, abort
import os

from flask_pymongo import PyMongo

application = Flask(__name__)
with application.app_context():
    mongo = PyMongo(application)
    d = mongo.db.classes

course,teacher,student='Calculus 1 (Science)','Joseph Rinehart','Raffi Hotter'

info = d.find({'name':course},{'_id':0,'notes':1})

notes=[]
for i in info[0]['notes']:
    if i['teacher']==teacher and i['student']==student:
        for j in i['files']:
            notes.append(j['name'][:-4])
        break;
notes.sort()
print(notes)

# def getClasses():
#     classes_curs = ex.find({},{'name':1,'_id':0}).sort('name',1)
#     classes = []
#     for cl in classes_curs:
#         classes.append(cl['name'])
#     return classes
#
# @application.route("/")
# def index():
#     classes=getClasses()
#     return classes[0]
#
# dat='2018-05-30'
# for course in next(os.walk('static/pdf/Notes'))[1]:
#     i=0
#     c = {
#         'name': course,
#         'notes': []
#         }
#     for teacher in next(os.walk('static/pdf/Notes/%s' % course))[1]:
#         for student in next(os.walk('static/pdf/Notes/%s/%s' % (course,teacher)))[1]:
#             c['notes'].append(
#                 {
#                     'teacher': teacher,
#                     'student': student,
#                     'date': dat,
#                     'files':[]
#                 })
#             path0 = "../static/pdf/Notes/" + course.replace(' ','%20') + "/" + teacher.replace(' ','%20') + "/" + student.replace(' ','%20') + "/"
#             for note in next(os.walk('static/pdf/Notes/%s/%s/%s/.' % (course,teacher,student)))[2]:
#                 if note != '.DS_Store':
#                     path = path0 + note.replace(' ','%20') + "'.pdf'"
#                     c['notes'][i]['files'].append(
#                     {
#                         'name': note,
#                         'path': path
#                     })
#             i+=1
#
#     ex.insert(c)



# c = {
#     'name': 'course',
#     'notes': [
#         {
#             'teacher': 'teacher',
#             'student': 'student',
#             'date': date,
#             'files': [
#                 {
#                     'name': '2',
#                     'path': '2'
#                 }
#             ]
#         }
#     ]
# }
