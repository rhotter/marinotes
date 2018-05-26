import os

course = 'Calculus 1'
teacher = 'Joseph Rinehart'
student = 'Raffi Hotter'

notes = next(os.walk('static/pdf/Notes/%s/%s/%s/.' % (course,teacher,student)))[2]
print(notes)
