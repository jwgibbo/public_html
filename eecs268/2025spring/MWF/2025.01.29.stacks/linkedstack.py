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
