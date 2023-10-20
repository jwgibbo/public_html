#main.py

from bst import BST
from course import Course


def main():
    my_bst = BST()

    course1 = Course('EECS', 168, 4.0, 'Gibbons')
    my_bst.add(course1)
    #let's assume we add a bunch of
    #Course objects to the bst

    try:
        next_course = my_bst.search(388)
        #If we make it here, we found the course
    except:
        #Course was not there!
