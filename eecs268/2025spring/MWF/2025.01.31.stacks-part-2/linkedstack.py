#linkedstack.py

from node import Node

class LinkedStack:
    def __init__(self):
        self._top = None #empty stack

    def is_empty(self):
        return self._top is None

    def push(self, entry):
        #put the entry in a node
        #put the node on top

    def pop(self):
        #remove and return the popped
        #value OR raise a RuntimeError
        #if the stack is empty

    def peek(self):
        #return top-most value or
        #raise a RuntimeError
