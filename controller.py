import csv

import student
import exam_result
import classroom

class Controller():
    def __init__(self):
        self.student_list = []
        self.exam_list = []
        self.literature_member_list = []
        self.science_member_list = []
        self.failure_list = []

    def read_student_information(self):
        if self.student_list is not None:
            self.student_list = []

        with open('data/student.csv', 'r') as data_stu:
            reader = csv.reader(data_stu)
            ls = [row for row in reader]

        for i in range(1, len(ls)+1):
            st = student.Student(i, ls[i-1][0], ls[i-1][1])
            self.student_list.append(st)

    def enter_exam(self, students):
        print("Please enter the student's score.")
        for student in students:
            print(student)
            japanese = input('japanese:')
            math = input('math:')
            english = input('english:')
            science = input('science:')
            society = input('society:')
            total = int(math) + int(japanese) + int(english) + int(science) + int(society)
            science_subject = int(math) + int(english) + int(science)
            cultural_subject = int(japanese) + int(english) +int(society)
            ex = exam_result.Exam_result(student, japanese, math, english, science, society, total, science_subject, cultural_subject)
            self.exam_list.append(ex)
        print('Thank you!')

    def division_class(self):
        number = 1
        number_2 = 1
        for i in range(1, len(self.student_list)+1):
            if self.student_list[i-1].get_major() == '2':
                name = self.student_list[i-1].get_name()
                total = self.exam_list[i-1].get_total()
                major_score = self.exam_list[i-1].get_cultural_subject()
                class_member = classroom.LiteratureClassRoom(number, name, total, major_score)
                self.literature_member_list.append(class_member)
                number += 1

            elif self.student_list[i-1].get_major() == '1':
                name = self.student_list[i-1].get_name()
                total = self.exam_list[i-1].get_total()
                major_score = self.exam_list[i-1].get_science_subject()
                class_member = classroom.ScienceClassRoom(number_2, name, total, major_score)
                self.science_member_list.append(class_member)
                number_2 += 1

            else:
                name = self.student_list[i-1].get_name()
                total = self.exam_list[i-1].get_total()
                wish_major = self.student_list[i-1].get_wish_major()
                if wish_major == '1':
                    major_score = self.exam_list[i-1].get_science_subject()
                elif wish_major == '2':
                    major_score = self.exam_list[i-1].get_cultural_subject()
                class_member = classroom.FailureStudentList(name, total, wish_major, major_score)
                self.failure_list.append(class_member)

    def show_result(self, science_member, literature_member, failure_member):
        print('-------------------------------------------------------------------')
        print('science-class-member')
        for member in science_member:
            print(member)
        print('-------------------------------------------------------------------')

        print('-------------------------------------------------------------------')
        print('literature-class-member')
        for member in literature_member:
            print(member)
        print('-------------------------------------------------------------------')

        print('-------------------------------------------------------------------')
        print('failure-student')
        for member in failure_member:
            print(member)
        print('-------------------------------------------------------------------')