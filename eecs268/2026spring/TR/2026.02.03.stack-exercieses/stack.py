#stack.py

from node import Node

class Stack:
    def __init__(self):
        self._top = None #empty stack

    def is_empty(self):
        return self._top is None

    def push(self, entry):
        new_top = Node(entry)
        #and then add this top the top
        #define this Thursday

    def pop(self):
        #define this Tuesday 2026.02.03
        #if the stack is stack is empty
        #raise a RuntimeError
        #otherwise remove the top node
        #and return its value

    def peek(self):
        #define this Tuesday 2026.02.03
        #if the stack is empty raise
        #a RuntimeError
        #otherwise return the top entry
