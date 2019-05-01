import student
import student_list

def main():
    while True:
        stu = student_list.Student_list()
        print('#####################')
        print(1, 'read student list')
        print(2, 'show student list')
        print(3, 'quit app')
        print('######################')
        number = input('choose number:')

        if number == '1':
            stu.read_exam()
        elif number == '2':
            stu.show_student_list()
        elif number == '3':
            print('Thank you.')
            break
        else:
            print('This number is not define.')

main()
