class Student:

    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def __str__(self):
        return self.student_id + " : " + self.student_name


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
