import exam
import student_list

class Exam_list():
    def __init__(self):
        self.exam_list = []

    def enter_exam(self):
        students = student_list.Student_list()
        students.read_exam()
        print("Please enter the student's score.")
        for student in students.student_list:
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