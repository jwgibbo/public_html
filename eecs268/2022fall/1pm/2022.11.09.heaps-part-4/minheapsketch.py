#minheapsketch.py


class MinHeap:
    def __init__(self):
        self._heap = []

    def add(self, entry):
        #Recall, we need to add the
        #entry to the lowest left-most
        #position
        self._heap.append(entry)
        self._upheap(index)

    def _upheap(self, index):
        #Compare against parent
        #swap if needed. Continue
        #upheaping
        #Define recursively

    def _downheap(self, index):
        #your definition here
