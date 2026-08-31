#linkedstack.py

from node import Node

class LinkedStack:
    def __init__(self):
        self._top = None

    def push(self, entry):
        #create a node, put the entry in
        #make the new node's next look
        # at the current top
        #make _top look at new node
