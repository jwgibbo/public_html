from node import Node

class Queue:
    def __init__(self):
        self._front = None
        self._back =  None

    def is_empty(self):
        return self._front == None

    def enqueue(self, entry):
        new_back = Node(entry)
        if self.is_empty():
            self._front = new_back
            self._back = new_back
        else:
            self._back.next = new_back
            self._back = new_back
            self._back.next = None

    def dequeue(self):
        #board work: define dequeue
        #return the value (if possible)
        

    
