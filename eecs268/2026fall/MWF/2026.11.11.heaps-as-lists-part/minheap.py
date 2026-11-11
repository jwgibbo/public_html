#minheap.py

class MinHeap:
    def __init__(self):
        self._heap = []


    def add(self, entry):
        #put the entry at the spot that
        #keeps the tree complete
        self._heap.append(entry)

        self._upheap(len(self._heap)-1)

    def _upheap(self, index):
        #define
        
