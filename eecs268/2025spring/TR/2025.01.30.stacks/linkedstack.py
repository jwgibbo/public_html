#stack.py
from node import Node

class LinkedStack:
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None
    
    def push(self, entry):
        #create a Node and store the entry
        #place Node at the top

    def pop(self):
        #remove top node
        #return the popped value
        #OR raise a RuntimeError

    def peek(self):
        #returns the value at the top
        #OR raises a RuntimeError if empty
