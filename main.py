import student
import student_list
import exam_list


def main():
    stu_ls = student_list.Student_list()
    stu_ls.read_exam()
    exam_ls = exam_list.Exam_list(stu_ls.student_list)
    exam_ls.cal_total_exam()
    exam_ls.cal_science_exam()
    exam_ls.cal_cultural_exam()

    if len(exam_ls.total_ls) == 0 and len(exam_ls.cultural_subject_ls) == 0 and len(exam_ls.science_subject_ls) == 0:
        return 'We can not judge because there is not enough information.'

    else:
        for i in range(1, len(exam_ls.total_ls)+1):
            if exam_ls.total_ls[i-1] >= 250:
                if stu_ls.student_list[i-1].get_wish_major() == '1':
                    if exam_ls.science_subject_ls[i-1] >= 200:
                        exam_ls.successful_candidate_list.append(i)
                    else:
                        exam_ls.rejected_list.append(i)
                elif stu_ls.student_list[i-1].get_wish_major() == '2':
                    if exam_ls.cultural_subject_ls[i-1] >= 200:
                        exam_ls.successful_candidate_list.append(i)
                    else:
                        exam_ls.rejected_list.append(i)
            else:
                exam_ls.rejected_list.append(i)

    print('successful-member')
    print('-------------------------------------------------------------------')
    for i in range(1, len(exam_ls.successful_candidate_list)+1):
        print('No:{}, name:{}, total:{}, science-sub:{}, cultural-sub:{}'
              .format(i,
                      stu_ls.student_list[exam_ls.successful_candidate_list[i-1]-1].get_name(),
                      exam_ls.total_ls[exam_ls.successful_candidate_list[i-1]-1],
                      exam_ls.science_subject_ls[exam_ls.successful_candidate_list[i-1]-1],
                      exam_ls.cultural_subject_ls[exam_ls.successful_candidate_list[i-1]-1]))
    print('-------------------------------------------------------------------')

    print('reject-member')
    print('-------------------------------------------------------------------')
    for i in range(1, len(exam_ls.rejected_list)+1):
        print('No:{}, name:{}, total:{}, science-sub:{}, cultural-sub:{}'
              .format(i,
                      stu_ls.student_list[exam_ls.rejected_list[i-1]-1].get_name(),
                      exam_ls.total_ls[exam_ls.rejected_list[i-1]-1],
                      exam_ls.science_subject_ls[exam_ls.rejected_list[i-1]-1],
                      exam_ls.cultural_subject_ls[exam_ls.rejected_list[i-1]-1]))
    print('-------------------------------------------------------------------')


main()