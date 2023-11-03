#minheap.py

class MinHeap:
    def __init__(self):
        self._heap = []

    def add(self, entry):
        #place the entry in the lowest
        #left-most position
        self._heap.append(entry)

        #upheap
        self._upheap(len(self._heap)-1)

    def _upheap(self, index):
        pass
        #board work for Friday

    def remove(self):
        #store the current root
        #swap with the temp root
        #pop the old root
        #downheap temp
        #return removed value

    def _downheap(self, index):
        pass
        #Code in the heap lab
