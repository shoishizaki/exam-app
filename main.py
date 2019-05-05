import student
import student_list
import exam_list

def main():
    stu_ls = student_list.Student_list()
    exam_ls = exam_list.Exam_list()
    while True:
        print('#####################')
        print(1, 'read student list')
        print(2, 'show student list')
        print(3, 'entry student exam')
        print(4, 'show exam')
        print(5, 'quit app')
        print('######################')
        number = input('choose number:')

        if number == '1':
            stu_ls.read_exam()
        elif number == '2':
            stu_ls.show_student_list()
        elif number == '3':
            exam_ls.enter_exam()
        elif number == '4':
            exam_ls.show_exam()
        elif number == '5':
            print('Thank you.')
            break
        else:
            print('This number is not define.')

main()
