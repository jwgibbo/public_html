#maxheap.py


class MaxHeap:
    def __init__(self):
        self._heap = []

    def add(self, entry):
        self._heap.append(entry)
        self._upheap(len(self._heap)-1)

    def _upheap(self, index):
        #define Nov 17th
        
