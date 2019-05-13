class Jadge_exam():
    def jadge_exam(self,student, exam):
        for i in range(1, len(exam)+1):
            if exam[i-1].get_total() >= 250:
                if student[i-1].get_wish_major() == '1':
                    if exam[i-1].get_science_subject() >= 200:
                        student[i-1].set_major('1')
                    else:
                        student[i-1].set_major('0')
                elif student[i-1].get_wish_major() == '2':
                    if exam[i-1].get_cultural_subject() >= 200:
                        student[i-1].set_major('2')
                    else:
                        student[i - 1].set_major('0')
            else:
                student[i-1].set_major('0')