## Still needs course class

import sqlite3 as sql

conn = sql.connect('db.sqlite')


# test method, needs to be implemented for general use
def printAllStudentsEnrolledSemester():
    cursor = conn.execute("SELECT * FROM Enrolls_in JOIN Student S on S.student_ID = Enrolls_in.student_ID")
    for row in cursor:
        print(row)


class Student:

    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def __str__(self):
        # Formating a string with students
        return "ID:%s, NAME:%s" % (self.student_id, self.student_name)

    @classmethod
    def getAll(self):
        result = []
        q = "SELECT * FROM Student"
        cursor = conn.execute(q)
        for row in cursor:
            student = Student(row[0], row[1])
            result.append(student)
        return result

    @classmethod
    def add(self, studentID, studentName):

        try:
            q = "INSERT INTO Student(student_ID,student_name) VALUES (?,?)"
            conn.execute(q, (studentID, studentName))
            conn.commit()
        except:
            print("That name or ID already exists in this table")

    @classmethod
    def remove(self, studentID):
        q2 = "SELECT * FROM Student WHERE student_ID = (?)"
        response = conn.execute(q2, (studentID,))
        if len(response.fetchall()) > 0:
            q = "DELETE FROM Student WHERE student_ID = (?)"
            conn.execute(q, (studentID,))
            conn.commit()
            return 1
        else:
            return 0

    @classmethod
    def editStudentInfo(self, studentName, studentID):
        rq = "SELECT * FROM Student WHERE student_ID = (?)"

        response = conn.execute(rq, (studentID,))
        if (len(response.fetchall()) > 0):
            q = "UPDATE Student Set student_name=(?) WHERE student_ID==(?)"
            conn.execute(q, (studentName, studentID))
            return 1
        else:
            return 0
            # No ID of that in student

    def getEnrolledCreds(self,studentID):
        q = "SELECT "


class Instructor:
    def __init__(self, instructor_id, instructor_name):
        self.instructor_id = instructor_id
        self.instructor_name = instructor_name

    def __str__(self):
        return "ID:%s, NAME:%s" % (self.instructor_id, self.instructor_name)

    @classmethod
    def getAll(self):
        result = []
        q = "SELECT * FROM Instructor"
        cursor = conn.execute(q)
        for row in cursor:
            instructor = Instructor(row[0], row[1])
            result.append(instructor)
        return result

    @classmethod
    def add(cls, instructorID, instructorName):

        try:
            q = "INSERT INTO main.Instructor(instructor_ID,instructor_name) VALUES (?,?)"
            conn.execute(q, (instructorID, instructorName))
            conn.commit()
        except:
            print("That name or ID already exists in this table")

    @classmethod
    def remove(cls, instructorID):
        q2 = "SELECT * FROM Instructor WHERE instructor_ID = (?)"
        response = conn.execute(q2, (instructorID,))
        if len(response.fetchall()) > 0:
            q = "DELETE FROM Instructor WHERE instructor_ID = (?)"
            conn.execute(q, (instructorID,))
            conn.commit()
            return 1
        else:
            return 0

    @classmethod
    def editInstructorInfo(cls,instructorName,instructorID):
        q = "SELECT * FROM Instructor WHERE instructor_ID = (?)"
        response = conn.execute(q, (instructorID,))
        if len(response.fetchall()) > 0:
            q2 = "UPDATE Instructor Set instructor_name=(?) WHERE instructor_ID==(?)"
            conn.execute(q2, (instructorName, instructorID))
            conn.commit()
            return 1
        else:
            return 0

#Instructor.editInstructor("Kelly Manso",60)
x = Instructor.getAll()
xSize = len(x)
for i in range(xSize):
     print(x[i])

class Enrollment:
    def __init__(self, student_id, section_id):
        self.student_id = student_id
        self.section_id = section_id
        self.flag = None

    @classmethod
    def getCourseLink(cls, section_id, course_id):
        q = "SELECT course_link FROM Section WHERE section_ID=? AND course_ID=?"
        cursor = conn.execute(q,(section_id,course_id))
        if len(cursor)<1:
            return 0
        else:
            cursor.fetchall()
            return cursor.fetchall()[0]

    def add(cls,flag, student_id, course_link):
        q = "INSERT INTO Enrolls_in(flag, student_ID, course_link) VALUES (?,?,?)"
        conn.execute(q,(flag,student_id,course_link))

    @classmethod
    def checkCap(cls,course_link):
        q = "SELECT capacity FROM Section WHERE course_link=?"
        capacity = conn.execute(q, course_link)
        return capacity.fetchall()[0]


class Section:
    def __init__(self, course_link, section_id, capacity,course_id, instructor_id ):
        self.course_link = course_link
        self.section_id = section_id
        self.capacity = capacity
        self.course_id = course_id
        self.instructor_id = instructor_id

