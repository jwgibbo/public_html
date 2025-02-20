#linkedlist.py

from node import Node

class LinkedList(self):
    def __init__(self):
        self._front = None
        self._length = 0

    def remove(self, index):
        #Define remove to either remove the node
        #at the given index, return the removed
        #value OR raise and IndexError
        
    def insert(self, index, entry):
        #Define this today (Tues Feb 11)
        #Insert the entry at the index OR
        #raise an IndexError if the index
        #if invalid

    def get_entry(self, index):
        target_node = self._get_node(index)
        return target_node.entry

    def length(self):
        return self._length

    def clear(self):
        #Empty the list
        self._front = None
        self._length = 0

    def _get_node(self, index):
        #Get a reference to node at index
        if index < 0 or index >= self._length:
            raise IndexError('Invalid index')
        else:
            target = self._front
            for num in range(index):
                target = target.next

            #target is a Node
            return target

