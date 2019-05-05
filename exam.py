class Exam():
    def __init__(self, student, japanese, math, english, science, society):
        self.student = student
        self.japanese = japanese
        self.math = math
        self.english = english
        self.science = science
        self.society = society

    def __str__(self):
        return 'name:{}, japanese:{},math:{}, english:{}, science:{}, society:{}'\
            .format(self.student,
                    self.japanese,
                    self.math,
                    self.english,
                    self.science,
                    self.society)

    def get_name(self):
        return self.student

    def get_japanese(self):
        return self.japanese

    def get_math(self):
        return self.math

    def get_english(self):
        return self.english

    def get_science(self):
        return self.science

    def get_society(self):
        return self.society

    def set_name(self, student):
        self.student = student

    def set_japanese(self, japanese):
        self.japanese = japanese

    def set_math(self, math):
        self.math = math

    def set_english(self, english):
        self.english = english

    def set_science(self,science):
        self.science = science

    def set_society(self, society):
        self.society = society