#minheap.py

class Minheap:
    def __init__(self):
        self._heap = []

    def add(self, entry):
        #place new value at the "lowest left-most"
        #position
        self._heap.append(entry)

        #upheap
        self._upheap(len(self._heap)-1)

    def _upheap(self, index):
        #Friday board work
        pass

    def remove(self):
        #store the current root
        #swap with temp root
        #pop the old root
        #downheap the temp root
        #Friday board

    def _downheap(self, index):
        #Done the heap lab
