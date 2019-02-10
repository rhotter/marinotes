from flask import Flask
from flask_pymongo import PyMongo
from config import S3_KEY, S3_SECRET, S3_BUCKET
import boto3

application = Flask(__name__)

# application.config['MONGO_DBNAME'] = 'server2'
application.config["MONGO_URI"] = "mongodb+srv://marinotes:Karelthedog123@marinotes0-khium.mongodb.net/test?retryWrites=true"

with application.app_context():
    mongo = PyMongo(application)
    d = mongo.db.classes

def name_to_id(class_name):
    return class_name.replace(' ', '%20')

def id_to_name(class_id):
    return class_id.replace('%20', ' ')

def upload_notes(class_name, teacher, author, date, file_names, files=None,
                approved=False):
    # Figure out how much has already been stored
    class_info = d.find_one({'_id': name_to_id(class_name)})
    teacher_info = None
    existing_teacher = True
    if class_info:
        existing_class = True
        teacher_id_array = [{'_id': teacher_id} for teacher_id in class_info['children']]
        # if teacher_id_array:
        #     teacher_info = d.find_one({'$or': teacher_id_array})
    else:
        class_info_id = d.insert({'_id': name_to_id(class_name),
                               'type': 'class',
                               'class': class_name,
                               'children': [],
                               'parent': 'classes',
                               'approved': True })
        class_info = d.find_one({'_id': class_info_id})
        class_list = d.find_one({'_id': 'classes'})
        d.update_one({'_id': 'classes'},
                     {'$set':
                         {'children':
                             class_list['children'].append(class_info['_id'])}})
    if not teacher_info:
        existing_teacher = False
        teacher_info_id = d.insert({'type': 'teacher',
                                 'teacher': teacher,
                                 'children': [],
                                 'parent': class_info['_id'],
                                 'approved': approved })
        teacher_info = d.find_one({'_id': teacher_info_id})

    author_info_id = d.insert({'type': 'author',
                            'author': author,
                            'date': date,
                            'children': [],
                            'parent': teacher_info['_id'],
                            'approved': approved })
    author_info = d.find_one({'_id': author_info_id})
    file_ids = []
    for file_name in file_names:
        file_ids.append(d.insert({'type': 'note',
                                  'name': file_name,
                                  'parent': author_info['_id'],
                                  'url': 'someUrl',
                                  'approved': approved}))
    # propagate back up to update children
    d.update_one({'_id': author_info['_id']},
                 {'$set':
                    {'children': file_ids}
                 })
    d.update_one({'_id': teacher_info['_id']},
              {'$set':
                 {'children':
                     teacher_info['children'].append(author_info['_id'])}
              })
    if not existing_teacher:
        d.update_one({'_id': class_info['_id']},
                {'$set':
                   {'children':
                       class_info['children'].append(teacher_info['_id'])}
                })

upload_notes('Calculus 3 (Science)', 'Joseph Rinehart', 'Raffi Hotter', 'March 3, 2018', ['Notes_1.pdf', 'Notes_2.pdf'])

def uploadFile(file, path):
    s3_resource = boto3.resource('s3', aws_access_key_id=S3_KEY, aws_secret_access_key=S3_SECRET)
    my_bucket = s3_resource.Bucket(S3_BUCKET)
    my_bucket.Object(path).put(Body=file) # can put name of file here

def deleteFile(file):
	s3_resource = boto3.resource('s3', aws_access_key_id=S3_KEY, aws_secret_access_key=S3_SECRET)
	my_bucket = s3_resource.Bucket(S3_BUCKET)
	my_bucket.Object(file).delete()







# """
# MongoDB functions
# """
#
# application.config['MONGO_DBNAME'] = 'server2'
#
# with application.app_context():
#     mongo = PyMongo(application)
#     d = mongo.db.classes
#
# def getClasses():
#     classes = []
#
#     classes_curs = d.find({},{'name':1,'_id':0}).sort('name',1)
#     for cl in classes_curs:
#         classes.append(cl['name'])
#     return classes
#
# def getInfo(course):
#     teachers, students = [],[]
#
#     info = d.find_one({'name':course},{'notes':1, '_id': 0})
#     for inf in info['notes']:
#         print(inf)
#         teachers.append(inf['teacher'])
#         students.append(inf['student'])
#     return teachers,students
#
# def getNotes(course,teacher,student):
#     # Architechture here should be redone. Not optimal
#     # for many notes in same class (which shouldn't be an issue)
#     info = d.find({'name':course},{'_id':0,'notes':1})
#
#     notes=[]
#     for i in info[0]['notes']:
#         if i['teacher']==teacher and i['student']==student:
#             for j in i['files']:
#                 notes.append(j['name'][:-4])
#             break;
#     notes.sort()
#     return notes
#
# """
# Amazon S3
# """
# def uploadFile(file, path):
#     s3_resource = boto3.resource('s3', aws_access_key_id=S3_KEY, aws_secret_access_key=S3_SECRET)
#     my_bucket = s3_resource.Bucket(S3_BUCKET)
#     my_bucket.Object(path).put(Body=file) # can put name of file here
#
# def deleteFile(file):
# 	s3_resource = boto3.resource('s3', aws_access_key_id=S3_KEY, aws_secret_access_key=S3_SECRET)
# 	my_bucket = s3_resource.Bucket(S3_BUCKET)
# 	my_bucket.Object(file).delete()
