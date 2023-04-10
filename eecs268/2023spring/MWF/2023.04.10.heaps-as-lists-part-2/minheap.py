#minheap.py

class Minheap:
    def __init__(self):
        self._heap = []

    def add(self, entry):
        #Append to keep tree complete
        self._heap.append(entry)

        #upheap
        self.upheap(len(self._heap)-1)

    def upheap(self, index):
        """Upheap value at given index"""
        
