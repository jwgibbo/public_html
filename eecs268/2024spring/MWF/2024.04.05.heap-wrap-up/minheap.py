#minheap.py

class MinHeap:
    def __init__(self):
        self._heap = []

    def add(self, entry):
        self._heap.append(entry)

        self._upheap(???)

    def _upheap(self, index):
        #define

    def _left_child_index(index):
        return 2*index+1
    
