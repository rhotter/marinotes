# Put data from folders into SQL database

import sqlite3, os
conn = sqlite3.connect('database.db')
c = conn.cursor()

# # print(classes[3:])
# for cl in classes[3:]:
#     c.execute("INSERT INTO courses (name) VALUES (?);",(cl,))
#     # print(cl)
#
# c.execute("SELECT * FROM courses WHERE name='Calculus 1'")
# c.execute("SELECT * FROM courses WHERE name='Calculus 2'")
#
# a = c.fetchone()
# print(a[0])


dat='2018-05-30'
for course in next(os.walk('static/pdf/Notes'))[1]:
    c.execute("SELECT courseID FROM courses WHERE name=?;",(course,))
    cl = c.fetchone()
    courseID = cl[0]

    for teacher in next(os.walk('static/pdf/Notes/%s' % course))[1]:
        c.execute("INSERT INTO teachers (name) VALUES (?);",(teacher,))

        c.execute("SELECT teacherID FROM teachers WHERE name=?;",(teacher,))
        t = c.fetchone()
        teacherID = t[0]

        for student in next(os.walk('static/pdf/Notes/%s/%s' % (course,teacher)))[1]:
            c.execute("INSERT INTO students (name) VALUES (?);",(student,))

            c.execute("SELECT studentID FROM students WHERE name=?;",(student,))
            s = c.fetchone()
            studentID = s[0]

            c.execute("INSERT INTO notes (courseID, teacherID, studentID, date) VALUES (?,?,?,?);",(courseID, teacherID, studentID, dat))

            # c.execute("SELECT noteID FROM notes WHERE courseID=? AND teacherID=? AND studentID=?;",(courseID, teacherID, studentID))
            c.execute("SELECT noteID FROM notes WHERE courseID=? AND teacherID=? AND studentID=? AND date=?;",(courseID, teacherID, studentID,dat))
            n = c.fetchone()
            noteID = n[0]
            path0 = "../static/pdf/Notes/" + course.replace(' ','%20') + "/" + teacher.replace(' ','%20') + "/" + student.replace(' ','%20') + "/"
            for note in next(os.walk('static/pdf/Notes/%s/%s/%s/.' % (course,teacher,student)))[2]:
                path = path0 + note.replace(' ','%20') + "'.pdf'"
                c.execute("INSERT INTO files (noteID, name, path) VALUES (?,?,?);",(noteID, note, path))

conn.commit()
conn.close()
