#linkedlist.py

from node import Node

class LinkedList:
    def __init__(self):
        self._front = None
        self._length = 0

    def insert(self, index, entry):
        #add the entry to the index
        #OR raise and IndexError

    def get_entry(self, index):
        if index < 0 or index >= self._length:
            raise IndexError('Invalid Index!')
        else:
            #traverse to the node at the index
            #return the entry
            #we'll finish this Wednesday
