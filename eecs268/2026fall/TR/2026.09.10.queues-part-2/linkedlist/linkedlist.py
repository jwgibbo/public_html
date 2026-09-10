#linkedlist.py

from node import Node

class LinkedList:
    def __init__(self):
        self._front = None
        self._length = 0

    def length(self):
        return self._length

    def clear(self):
        self._front = None
        self._length = 0

    def get_entry(self, index):
        #define Thur Sep 10
        
