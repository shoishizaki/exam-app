import exam

class Exam_list():
    def __init__(self):
        self.exam_list = []

    def enter_exam(self):
        print("Please enter the student's score.")
        name = input('name:')
        japanese = input('japanese:')
        math = input('math:')
        english = input('english:')
        science = input('science:')
        society = input('society:')
        ex = exam.Exam(name, japanese, math, english, science, society)
        self.exam_list.append(ex)
        print('Thank you!')

    def show_exam(self):
        if len(self.exam_list) == 0:
            print('There is not exam data.')

        else:
            for ls in self.exam_list:
                print('name:', ls.get_name(), ',', 'japanese:', ls.get_japanese(), ',',
                      'math:', ls.get_math(), ',', 'english:', ls.get_english(), ',',
                      'science:', ls.get_science(), ',', 'society:', ls.get_society())