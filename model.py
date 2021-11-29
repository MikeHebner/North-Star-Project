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

#
# def add(status, ID, name):
#     if status == "s":
#         try:
#
#             q = "INSERT INTO Student(student_ID,student_name) VALUES (?,?)"
#             conn.execute(q, (ID, name))
#             conn.commit()
#         except:
#             print("That name or ID already exists in this table")
#
#
#
#     elif status == "i":
#         try:
#             q = "INSERT INTO Instructor(instructor_ID, instructor_name) VALUES (?,?)"
#             conn.execute(q, (ID, name))
#             conn.commit()
#         except:
#             print("That name or ID already exists in this table")
#
#
# def remove(status, name):
#     if status == "student":
#
#         q = "DELETE FROM Student WHERE student_name = (?)"
#         conn.execute(q, (name,))
#         conn.commit()
#     elif status == "instructor":
#         q = "DELETE FROM Instructor WHERE instructor_name = (?)"
#         conn.execute(q, (name,))
#         conn.commit()

#
# add("s", 123, "Bobby")
# remove("student", "Bobby")
# Student.add(123, "Bobby")
# print(Student.remove("9045"))
# add("student", 123, "Bobby1")
# Student.editStudentInfo("OtherBobby", "123")
# x = Student.getAll()
# xSize = len(x)
# for i in range(xSize):
#     print(x[i])


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

Instructor.editInstructorInfo("Kelly Manso",60)
x = Instructor.getAll()
xSize = len(x)
for i in range(xSize):
     print(x[i])

class Enrollment:
    def __init__(self, student_id, section_id):
        self.student_id = student_id
        self.section_id = section_id
        self.flag = None

    def add(cls,student_id, section_id, flag):
        q = "INSERT INTO Enrolls_in(flag, student_ID, course_link) VALUES (?,?,?)"



class Section:
    def __init__(self, section_id, capacity, course_id,instuctor_id):
        self.section_id = section_id
        self.capacity = capacity
        self.course_id = course_id
        self.instructor_id = instuctor_id

    @classmethod
    def add(cls,section_id,capacity,course_id,instructor_ID):
        q1 = "SELECT * FROM main.Course WHERE course_ID=(?)"
        cursor = conn.execute(q1, (course_id,))
        if len(cursor.fetchall()) > 0:
            q2 = "SELECT * FROM main.Instructor WHERE instructor_ID=(?)"
            cursor2 = conn.execute(q2, (instructor_ID,))
            if len(cursor2.fetchall()) > 0:
                q3 = "SELECT * FROM main.Section WHERE section_ID=(?) and course_ID=(?)"
                cursor3 = conn.execute(q3, (section_id, course_id,))
                if len(cursor3.fetchall()) > 0:
                    return 2
                    #Duplicate Section is trying to be entered
                else:
                    q4 = "INSERT INTO Section(section_ID,capacity,course_ID,instructor_ID) VALUES (?,?,?,?)"
                    conn.execute(q4, (section_id,capacity,course_id,instructor_ID))
                    conn.commit()
                    return 1
                    #Section is valid and added
            else:
                return 3
                #No instructor has that ID
        else:
            return 4
            #No Course has that ID
    @classmethod
    def remove(cls,section_id,course_id,instructor_ID):
        q = "SELECT * FROM main.Section WHERE section_ID=(?) and course_ID=(?) and instructor_ID=(?)"
        response = conn.execute(q, (section_id, course_id, instructor_ID))
        if len(response.fetchall())>0:
            q2 = "DELETE FROM main.Section WHERE section_ID=(?) and course_ID=(?) and instructor_ID=(?)"
            conn.execute(q2, (section_id, course_id, instructor_ID))
            conn.commit()
            return 1
            #Successfully found and deleted section
        else:
            return 0
            #Did invalid section
    @classmethod
    def editSectionInfo(cls,section_ID,course_ID, instructor_ID):
        q = "SELECT * FROM main.Section WHERE section_ID=(?) and course_ID=(?)"
        response = conn.execute(q, (section_ID,course_ID,))
        if len(response.fetchall())>0:
            q2 = "SELECT * FROM main.Instructor WHERE instructor_ID=(?)"
            response2 = conn.execute(q2, (instructor_ID,))
            if len(response2.fetchall())>0:
                q3 = "UPDATE Section Set instructor_ID=(?) WHERE main.Section.section_ID==(?) and main.Section.course_ID==(?)"
                conn.execute(q3, (instructor_ID,section_ID,course_ID,))
                conn.commit()
                return 1
            else:
                return 2
                #No Instructor with that ID
        else:
            return 3
            #Section doesn't exist
print(Section.add(13,3,"ART101",30))
print(Section.remove(13,"ART101",10))
print(Section.editSectionInfo(13,"ART101",10))