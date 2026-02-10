#linkedqueue.py

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
        #define this 2026.02.05

    def dequeue(self):
        #define this 2026.02.05

    def peek_front(self):
        #define this 2026.02.10
