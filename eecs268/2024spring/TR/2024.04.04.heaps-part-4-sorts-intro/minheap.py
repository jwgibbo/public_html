#minheap.py

class MinHeap:
    def __init__(self):
        self._heap = []

    def add(self, entry):
        #keep the "tree" complete
        self._heap.append(entry)

        #upheap the new value
        self._upheap(???)

    def _upheap(self, index):
        #define this

    def remove(self):
        #next week's lab

    def length(self):
        #next week's lab

    def _downheap(self, index):
        #next week's lab
