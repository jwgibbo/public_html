#minheap.py


class MinHeap:
    def __init__(self):
        self._heap = []

    def add(self, entry):
        #Keep the "heap" complete
        self._heap.append(entry)
        self._upheap(len(self._heap)-1)

    def _upheap(self, index):
        '''Upheaps value at given index
            to the correct position'''
        #Write a recursive definition

    def _left_child(self, index):
        #return index of left child of i

    def _right_child(self, index):
        #return index of right child of i

    def _downheap(self, index):
    
