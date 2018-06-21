# Put data from folders into SQL database

import sqlite3, os
conn = sqlite3.connect('database-upd3.db')
c = conn.cursor()

dat='2018-05-30'
c.execute("CREATE TABLE courses (courseID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, courseName TEXT NOT NULL)")
c.execute("CREATE TABLE files (fileID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, noteID INTEGER NOT NULL, fileName TEXT NOT NULL, path TEXT NOT NULL, FOREIGN KEY(noteID) REFERENCES notes(noteID))")
c.execute("CREATE TABLE notes (noteID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, courseID INTEGER NOT NULL, teacherID INTEGER NOT NULL, studentID INTEGER NOT NULL, date TEXT NOT NULL, FOREIGN KEY(courseID) REFERENCES courses(courseID), FOREIGN KEY(teacherID) REFERENCES teachers(teacherID), FOREIGN KEY(studentID) REFERENCES students(studentID))")
c.execute("CREATE TABLE students(studentID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, studentName TEXT NOT NULL)")
c.execute("CREATE TABLE teachers(teacherID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, teacherName TEXT NOT NULL)")

for course in next(os.walk('static/pdf/Notes'))[1]:
    c.execute("INSERT INTO courses (courseName) VALUES (?);",(course,))
    c.execute("SELECT courseID FROM courses WHERE courseName=?;",(course,))
    cl = c.fetchone()
    courseID = cl[0]

    for teacher in next(os.walk('static/pdf/Notes/%s' % course))[1]:
        c.execute("INSERT INTO teachers (teacherName) VALUES (?);",(teacher,))

        c.execute("SELECT teacherID FROM teachers WHERE teacherName=?;",(teacher,))
        t = c.fetchone()
        teacherID = t[0]

        for student in next(os.walk('static/pdf/Notes/%s/%s' % (course,teacher)))[1]:
            c.execute("INSERT INTO students (studentName) VALUES (?);",(student,))

            c.execute("SELECT studentID FROM students WHERE studentName=?;",(student,))
            s = c.fetchone()
            studentID = s[0]

            c.execute("INSERT INTO notes (courseID, teacherID, studentID, date) VALUES (?,?,?,?);",(courseID, teacherID, studentID, dat))

            c.execute("SELECT noteID FROM notes WHERE courseID=? AND teacherID=? AND studentID=? AND date=?;",(courseID, teacherID, studentID,dat))
            n = c.fetchone()
            noteID = n[0]
            path0 = "../static/pdf/Notes/" + course.replace(' ','%20') + "/" + teacher.replace(' ','%20') + "/" + student.replace(' ','%20') + "/"
            for note in next(os.walk('static/pdf/Notes/%s/%s/%s/.' % (course,teacher,student)))[2]:
                if note != '.DS_Store':
                    path = path0 + note.replace(' ','%20') + "'.pdf'"
                    c.execute("INSERT INTO files (noteID, fileName, path) VALUES (?,?,?);",(noteID, note, path))

c.execute("CREATE UNIQUE INDEX `idx_courses` ON `courses` ( `courseName` ASC )")
c.execute("CREATE INDEX `idx_notes` ON `files` ( `noteID` ASC )")

conn.commit()
conn.close()
