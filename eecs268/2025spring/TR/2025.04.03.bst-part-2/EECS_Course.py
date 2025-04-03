#EECS_Course.py


class EECS_Course:
    def __init__(self, ???):
        self.course_num = ???
        self.professor = ???
        self.credit = ???
        self.difficulty = ???

    def __lt__(self, other):
        if isinstance(other, int):
            #course < int
            #Used for searching
            return self.course_num < other
        else:
            #course < course
            #Used for adding
            return self.course_num < other.course_num

    #define __gt__ and __eq__
