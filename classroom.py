class LiteratureClassRoom():
    def __init__(self,number, name, total, major_score):
        self.number = number
        self.name = name
        self.total = total
        self.major_score = major_score

    def get_name(self):
        return self.name

    def get_total(self):
        return self.total

    def get_major_score(self):
        return self.major_score

    def __str__(self):
        return 'No:{}, name:{}, total:{}, major-score:{}'\
            .format(self.number,
                    self.name,
                    self.total,
                    self.major_score)

class ScienceClassRoom():
    def __init__(self,number, name, total, major_score):
        self.number = number
        self.name = name
        self.total = total
        self.major_score = major_score

    def get_name(self):
        return self.name

    def get_total(self):
        return self.total

    def get_major_score(self):
        return self.major_score

    def __str__(self):
        return 'No:{}, name:{}, total:{}, major-score:{}'\
            .format(self.number,
                    self.name,
                    self.total,
                    self.major_score)



class FailureStudentList():
    def __init__(self, name, total, wish_major, major_score):
        self.name = name
        self.total = total
        self.wish_major = wish_major
        self.major_score = major_score

    def get_name(self):
        return self.name

    def get_total(self):
        return self.total

    def get_wish_major(self):
        return self.wish_major

    def get_major_score(self):
        return self.major_score

    def __str__(self):
        return 'name:{}, total:{}, wish-major:{}, major-score:{}'\
            .format(self.name,
                    self.total,
                    self.wish_major,
                    self.major_score)