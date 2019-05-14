class Exam_result():
    def __init__(self, student, japanese, math, english, science, society, total, science_subject, cultural_subject):
        self.student = student
        self.japanese = japanese
        self.math = math
        self.english = english
        self.science = science
        self.society = society
        self.total = total
        self.science_subject = science_subject
        self.cultural_subject = cultural_subject

    def __str__(self):
        return 'name:{}, japanese:{},math:{}, english:{}, science:{}, society:{}'\
            .format(self.student,
                    self.japanese,
                    self.math,
                    self.english,
                    self.science,
                    self.society)

    def get_student(self):
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

    def get_total(self):
        return self.total

    def get_science_subject(self):
        return self.science_subject

    def get_cultural_subject(self):
        return self.cultural_subject