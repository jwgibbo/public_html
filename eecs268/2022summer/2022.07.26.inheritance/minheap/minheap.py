#minheap.py

class MinHeap:
    def __init__(self):
        self._heap = []

    def add(self, entry):
        self._heap.append(entry)
        self.upheap(len(self._heap)-1)

    def _upheap(self, index):
        #compare with parent's value
        #swap if needed
        #continue upheap
