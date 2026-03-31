#eecscourse.py

class EECS_Course:
    def __init__(self):
        self.prof = ???
        self.course_num = ???
        self.credits = ???
        self.required = ???

    def __lt__(self, other):
        return self.course_num < other.course_num
