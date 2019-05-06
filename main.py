import student
import student_list
import exam_list
    
    
def main():
    stu_ls = student_list.Student_list()
    stu_ls.read_exam()

    exam_ls = exam_list.Exam_list(stu_ls.student_list)

main()
