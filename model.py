class Student(object):

    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def get_name(self):
        return self.student_name


class Instructor(object):

    def __init__(self, instructor_id, instructor_name):
        self.instructor_id = instructor_id
        self.instructor_name = instructor_name

    def get_name(self):
        return self.instructor_name


class Enrollment(object):

    def __init__(self, student_id, section_id, flag):
        self.student_id = student_id
        self.section_id = section_id
        self.flag = None

    def addFlag(self):
        pass

    def removeFlag(self):
        pass


class Section(object):
    def __init__(self, section_id, capacity, credits):
        self.section_id = section_id
        self.capacity = capacity
        self.credits = credits



