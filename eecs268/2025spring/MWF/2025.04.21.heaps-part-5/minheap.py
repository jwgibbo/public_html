#minheap.py

#We don't use BinaryNode class

class MinHeap:
    def __init__(self):
        self._heap = []

    def add(self, entry):
        self._heap.append(entry)
        self._upheap(len(self._heap)-1)

    def _upheap(self, index):
        #compare the value at index to its parent
        #swap if needed. Recurse on the new index
        #if swap occured.
        
        
