#stack.py

from node import Node

class Stack:
    def __init__(self):
        self._top = None #empty stack

    def is_empty(self):
        if self._top is None:
            return True
        else:
            return False

    def push(self, entry):
        #Create a new Node; add entry
        #Make it top-most node without
        #losing track of current top
        
        

    def pop(self):
        #define (Thursday 2025.08.28)

    def peek(self):
        #return the top-most value OR
        #raise a RuntimeError with message 'Stack empty'
