class Person(object):

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_name(self):
        return self.name

    def is_instructor(self):
        return False


class Instructor(Person):

    def is_instructor(self):
        return True


class Student(Person):

    def is_instructor(self):
        return False


class Registration:
    pass

