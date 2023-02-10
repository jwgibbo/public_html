#linkedlist.py

from node import Node

class LinkedList:
    def __init__(self):
        self._front = None
        self._length = 0

    def insert(self, index, entry):
        #We're waiting on this

    def get_entry(self, index):
        #Validate the index
        #If it's invalid raise IndexError
        if 0 <= index and index < self._length:
            #If the index is valid, traverse
            #  to that index
            #Start jumper at the front
            jumper = self._front
            for num in range(index):
                jumper = jumper.next
            #jumper is referring to the node at
            #the given index
            return jumper.entry
        else:
            raise IndexError('Invalid Index')
