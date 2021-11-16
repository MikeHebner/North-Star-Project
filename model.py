import sqlite3 as sql

conn = sql.connect('identifier.sqlite')


def printSemester():
    cursor = conn.execute("SELECT * FROM Enrolls_in JOIN Student S on S.student_ID = Enrolls_in.student_ID")
    for row in cursor:
        print(row)


printSemester()


class Student:

    def __init__(self, student_id=None, student_name=None):
        self.student_id = student_id
        self.student_name = student_name

    def __str__(self):
        return ("%s:%s" % (self.student_id,self.student_name))

    @classmethod
    def getAll(self):
        result = []
        q = "SELECT * FROM Student"
        cursor = conn.execute(q)
        for row in cursor:
            student = Student(row[1], row[0])
            result.append(student)
        return result

x = Student.getAll()
print(x[1].student_name)


class Instructor:
    def __init__(self, instructor_id, instructor_name):
        self.instructor_id = instructor_id
        self.instructor_name = instructor_name

    def __str__(self):
        return self.instructor_id + " : " + self.instructor_name


class Enrollment:
    def __init__(self, student_id, section_id):
        self.student_id = student_id
        self.section_id = section_id
        self.flag = []

    def addFlag(self, flag):
        self.flag.append(flag)

    def removeFlag(self, flag):
        self.flag.remove(flag)


class Section:
    def __init__(self, section_id, capacity, credits):
        self.section_id = section_id
        self.capacity = capacity
        self.credits = credits
