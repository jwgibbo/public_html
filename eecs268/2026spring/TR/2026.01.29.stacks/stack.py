#stack.py

from node import Node

class Stack:
    def __init__(self):
        self._top = None #empty stack

    def is_empty(self):
        return self._top is None

    def push(self, entry):
        #define this
