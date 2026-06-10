#linkedqueue.py

from node import Node

class LinkedQueue:
    def __init__(self):
        self._front = None
        self._back = None

    def enqueue(self, entry):
        #define here

    def is_empty(self):
        if self._front is None and self._back is None:
            return True
        else:
            return

    def peek_front(self):
        if self.is_empty():
            raise RuntimeError('Queue empty')
        else:
            return self._front.entry
        
