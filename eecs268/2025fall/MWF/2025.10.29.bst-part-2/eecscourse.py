#eecscourse.py

class EECS_Course:
    def __init__(self):
        self.course_num = ???
        self.professor = ???
        self.credits = ???
        self.is_required = ???

    def __lt__(self, other):
        if self.course_num < other.course_num:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.course_num > other.course_num:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.course_num == other.course_num:
            return True
        else:
            return False
