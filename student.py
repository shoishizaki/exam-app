class Student():
    def __init__(self, student_id, name, wish_major):
        self.student_id = student_id
        self.name = name
        self.wish_major = wish_major
        self.major = ""

    def get_student_id(self):
        return self.student_id

    def get_name(self):
        return self.name

    def get_wish_major(self):
        return self.wish_major

    def get_major(self):
        return self.major

    def set_major(self, major):
        self.major = major
