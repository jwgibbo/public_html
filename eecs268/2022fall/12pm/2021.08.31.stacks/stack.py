#stack.py

from node import Node

class Stack:
    def __init__(self):
        self._top = None

    def push(self, entry):
        #create a node with the entry
        #put it on the top
