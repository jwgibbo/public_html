#stack.py
from node import Node

class LinkedStack:
    def __init__(self):
        self._top = None

    def push(self, entry):
        #create a Node and store the entry
        #place Node at the top
