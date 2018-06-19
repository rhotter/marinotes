import sqlite3, os
conn = sqlite3.connect('database.db')
c = conn.cursor()

classes = next(os.walk('static/pdf/Notes'))[1]
# # print(classes[3:])
# for cl in classes[3:]:
#     c.execute("INSERT INTO courses (name) VALUES (?);",(cl,))
#     # print(cl)

c.execute("SELECT * FROM courses WHERE name='Calculus 1'")
c.execute("SELECT * FROM courses WHERE name='Calculus 2'")

a = c.fetchone()
print(a[0])

for course in classes:
    for teacher in next(os.walk('static/pdf/Notes/%s' % course))[1]:
        for student in next(os.walk('static/pdf/Notes/%s/%s' % (course,teacher)))[1]:
            for note in next(os.walk('static/pdf/Notes/%s/%s/%s/.' % (course,teacher,student)))[2]:
                c.execute("INSERT INTO teachers (name) VALUES (?);",(teacher,))
                c.execute("INSERT INTO students (name) VALUES (?);",(student,))
                c.execute("SELECT * FROM teachers WHERE name=?",(teacher,))
                t = c.fetchone()
                teacherID = a[0]

                c.execute("SELECT * FROM students WHERE name=?",(student,))
                s = c.fetchone()
                studentID = a[0]
    return teachers,students

conn.commit()
conn.close()
