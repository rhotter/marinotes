# Put data from folders into MongoDB database

from flask import Flask
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
with app.app_context():
    mongo = PyMongo(app)
    ex = mongo.db.classes

# classes_curs = ex.find({},{'name':1,'_id':0}).sort('name',1)
# classes = []
# for cl in classes_curs:
#     classes.append(cl['name'])
# print(classes)


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
        #             'files': [
        #                 {
        #                     'name': '2',
        #                     'path': '2'
        #                 }
        #             ]
        #         }
        #     ]
        # }
