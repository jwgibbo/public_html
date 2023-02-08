#linkedlist.py

from node import Node

class LinkedList:
    def __init__(self):
        self._front = None
        self._length = 0

    def insert(self, index, entry):
        #we'll wait on this

    def get_entry(self, index):
        #make sure index is valid
        #if not, raise IndexError
        
        #where jumper starts
        jumper = self._front
