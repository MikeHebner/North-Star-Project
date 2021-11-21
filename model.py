## Still needs course class

import sqlite3 as sql

conn = sql.connect('identifier.sqlite')


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
    def add(self,studentID,studentName):


        q = "INSERT INTO Student(student_ID,student_name) VALUES (?,?)"
        cursor = conn.execute(q,(studentID,studentName))
    @classmethod
    def remove(self,studentName):
        q = "DELETE FROM Student WHERE student_name = (?)"
        conn.execute(q, (studentName,))
    #@classmethod
   # def editStudentInfo(self,studentName,studentID):
       # q = "UPDATE Student "


Student.add(123,"Kyle Stearns")
Student.remove("Kyle Stearns")
x = Student.getAll()
xSize = len(x)
for i in range(xSize):
    print(x[i])



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


y = Instructor.getAll()


class Enrollment:
    def __init__(self, student_id, section_id):
        self.student_id = student_id
        self.section_id = section_id
        self.flag = None


class Section:
    def __init__(self, section_id, capacity, credits):
        self.section_id = section_id
        self.capacity = capacity
        self.credits = credits
