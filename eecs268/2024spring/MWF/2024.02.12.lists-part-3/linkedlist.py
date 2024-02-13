#linkedlist.py

from node import Node

class LinkedList:
    def __init__(self):
        self._front = None
        self._length = 0

    def get_entry(self, index):
        #defined last class

    def insert(self, index, entry):
        #define this

    def remove(self, index):
        #check the index
        if index < 0 or index >= self._length:
            raise IndexError('Invalid index')
        elif index == 0:
            old_front = self._front
            self._front = self._front.next
            self._length = self._length - 1
            return old_front.entry
        else:
            before = self._front
            for _ in range(index-1):
                before = before.next

            target = before.next
            after = target.next

            before.next = after
            self._length = self.length - 1
            return target.entry
