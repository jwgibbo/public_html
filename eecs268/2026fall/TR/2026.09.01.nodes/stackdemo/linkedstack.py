#linkedstack.py

from node import Node

class LinkedStack:
    def __init__(self):
        self._top = None

    def push(self, entry):
        #create a node with the entry
        #connect new node to the top
        #make _top refers to new node
