#main.py
from course import Course
from bst import BST

def main():
    my_bst = BST()
    course1 = Course(388, 4.0, 'Luo')
    my_bst.add(course1)
    #assume we add more courses

    try:
        next_course = my_bst.search(388)
    except:
        #ut oh we didn't the course!
