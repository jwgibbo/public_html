#linkedstack.py

from node import Node

class LinkedStack:
    def __init__(self):
        self._top = None

    def push(self, entry):
        #1) create a node, put the entry in it
        #2) connect that node's next to what is already
        #   on top
        #3) make top look at the new node

    def is_empty(self):
        return self._top is None

    def peek(self):
        if self.is_empty():
            #there's nothing in the stack
            raise RuntimeError('stack empty')
        else:
            return self._top.entry

    def pop(self):
        #raise a RuntimeError if stack is empty
        #otherwise remove and return
        #  the top-most value
        
        
