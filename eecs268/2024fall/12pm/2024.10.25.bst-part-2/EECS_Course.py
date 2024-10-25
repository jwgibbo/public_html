#EECS_Course.py

class EECS_Course:
    def __init__(self, ???):
        #initial all member variables

    #any other methods

    def __lt__(self, other):
        if isinstance(other, int):
            return self.course_num < other
        else:
            return self.course_num < other.course_num
