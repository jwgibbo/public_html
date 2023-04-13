#minheap.py

class MinHeap:
    def __init__(self):
        sel        f._heap = []

    def add(self, entry):
        self._heap.append(entry)
        self._upheap(len(self._heap)-1)

    def _upheap(self, index):
        #upheap the value
        #at the given index
