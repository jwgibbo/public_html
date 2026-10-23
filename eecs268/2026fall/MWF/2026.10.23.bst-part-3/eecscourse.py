#eecscourse.py

class EECS_Course:
    def __init__(self, ???):
        self.course_num = ???
        self.prof = ???
        self.credits = ???

    def __lt__(self, other):
        return self.course_num < other.course_num

    def __gt__(self, other):
        return self.course_num > other.course_num

    def __eq__(self. other):
        return self.course_num == other.course_num
