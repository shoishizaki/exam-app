import csv

import student

class Student_list():
    def __init__(self):
        self.student_list = []

    def read_exam(self):
        with open('data/student.csv', 'r') as data_stu:
            reader = csv.reader(data_stu)
            ls = [row for row in reader]

        for i in range(1, len(ls)+1):
            st = student.Student(i, ls[i-1][0], ls[i-1][1])
            self.student_list.append(st)


    def show_student_list(self):
        for ls in self.student_list:
            print('----------------------------------')
            print('student_id:', ls.get_student_id())
            print('name:', ls.get_name())
            print('wish_major:', ls.get_wish_major())
            print('major:', ls.get_major())
            print('----------------------------------')