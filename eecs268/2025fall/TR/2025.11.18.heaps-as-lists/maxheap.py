#maxheap.py

class MaxHeap:
    def __init__(self):
        self._heap = []

    def add(self, entry):
        #put the new value at the end of the list
        self._heap.append(entry)

        #upheap the value
        self._upheap(len(self._heap)-1)

    def _upheap(self, index):
        #define Nov 18
        
