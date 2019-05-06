import exam
import student_list

class Exam_list():
    def __init__(self, students):
        self.exam_list = []
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