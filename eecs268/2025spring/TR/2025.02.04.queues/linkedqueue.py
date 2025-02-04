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
        ???

    def dequeue(self):
        #Either return the dequeued value
        #or raise a RuntimeError if empty
        
