import exam
import student

class Exam_list():
    def __init__(self, students):
        self.exam_list = []
        self.total_ls = []
        self.science_subject_ls = []
        self.cultural_subject_ls = []
        self.successful_candidate_list = []
        self.rejected_list = []
        self.enter_exam(students)

    def enter_exam(self, students):
        if len(students) == 0:
            print('There is no student date here.')
        
            return

        print("Please enter the student's score.")
        for student in students:
            print(student)
            japanese = input('japanese:')
            math = input('math:')
            english = input('english:')
            science = input('science:')
            society = input('society:')
            ex = exam.Exam(student, japanese, math, english, science, society)
            self.exam_list.append(ex)
        print('Thank you!')

    def show_exam(self):
        if len(self.exam_list) == 0:
            print('There is no exam data here.')

        else:
            for ls in self.exam_list:
                print('student: {student}, japanese: {japanese}, math: {math},'
                      ' english: {english}, science: {science},society: {society}'
                      .format(student=ls.student,
                              japanese=ls.get_japanese(),
                              math=ls.get_math(),
                              english=ls.get_english(),
                              science=ls.get_science(),
                              society=ls.get_society()))

    def cal_total_of_exam(self):
        for i in range(len(self.exam_list)):
            japanese = self.exam_list[i].get_japanese()
            math = self.exam_list[i].get_math()
            english = self.exam_list[i].get_english()
            science = self.exam_list[i].get_science()
            society = self.exam_list[i].get_society()
            total = int(japanese) + int(math) + int(english) + int(science) + int(society)
            self.total_ls.append(total)

    def cal_science_of_exam(self):

        for i in range(len(self.exam_list)):
            math = self.exam_list[i].get_math()
            english = self.exam_list[i].get_english()
            science = self.exam_list[i].get_science()
            total = int(math) + int(english) + int(science)
            self.science_subject_ls.append(total)

    def cal_cultural_of_exam(self):
        for i in range(len(self.exam_list)):
            japanese = self.exam_list[i].get_japanese()
            english = self.exam_list[i].get_english()
            society = self.exam_list[i].get_society()
            total = int(japanese) + int(english) + int(society)
            self.cultural_subject_ls.append(total)