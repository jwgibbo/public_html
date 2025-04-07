class EECS_Course:
    def __init__(self, ???):
        self.professor = ???
        self.credits = ???
        self.course_num = ???
        self.difficulty = ???
        #other data for the course

    def __lt__(self, other):
        if isinstance(other, int):
            #object < int
            return self.course_num < other 
        else:
            #object < object
            return self.course_num < other.course_num
