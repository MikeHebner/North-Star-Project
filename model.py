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

        try:
            q = "INSERT INTO Student(student_ID,student_name) VALUES (?,?)"
            cursor = conn.execute(q,(studentID,studentName))
        except:
            print("That name or ID already exists in this table")
    @classmethod
    def remove(self,studentName):
        q = "DELETE FROM Student WHERE student_name = (?)"
        conn.execute(q, (studentName,))

    @classmethod
    def editStudentInfo(self,infoType,studentName,studentID):
        if infoType=="ID":
            q = "UPDATE Student Set student_ID=(?) WHERE student_name==(?)"
            conn.execute(q, (studentID,studentName))
        elif infoType=="name":
            q = "UPDATE Student Set student_name=(?) WHERE student_ID==(?)"
            conn.execute(q, (studentName,studentID))
        else:
            print("Please use either ID or name")
            #testing else statement
def add(status,ID,name):
    if status=="student":
        try:

            q = "INSERT INTO Student(student_ID,student_name) VALUES (?,?)"
            conn.execute(q, (ID, name))
        except:
            print("That name or ID already exists in this table")



    elif status=="instructor":
        try:
            q = "INSERT INTO Instructor(instructor_ID, instructor_name) VALUES (?,?)"
            conn.execute(q, (ID, name))
        except:
            print("That name or ID already exists in this table")
def remove(status,name):
    if status == "student":

            q = "DELETE FROM Student WHERE student_name = (?)"
            conn.execute(q, (name,))
    elif status == "instructor":
        q = "DELETE FROM Instructor WHERE instructor_name = (?)"
        conn.execute(q, (name,))

add("student",123,"Bobby")
remove("student","Bobby")
Student.add(123,"Bobby")
Student.remove("Roger Molinari")
add("student",123,"Bobby1")
Student.editStudentInfo("name","OtherBobby",123)
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
