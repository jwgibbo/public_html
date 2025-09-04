#linkedqueue.py

from node import Node

class LinkedQueue:
    def __init__(self):
        self._front = None
        self._back = None

    def is_empty(self):
        if self._front is None and self._back is None:
            return True
        else:
            return False

    def enqueue(self, entry):
         #define (Thur Sep 9)

    def dequeue(self):
        #define (Thur Sep 9)
