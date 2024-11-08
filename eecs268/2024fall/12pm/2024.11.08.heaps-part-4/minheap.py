#minheap.py

class MinHeap:
    def __init__(self):
        self._heap = [] #empty heap

    def add(self, entry):
        #Keep the heap complete
        self._heap.append(entry)

        self._upheap(len(self._heap)-1)

    def _upheap(self, index):
        #Define a recursive upheap
        #Compare against the parent,
        #  swap if needed
        #  Upheap as needed

    def remove(self):
        if len(self._heap) > 0:
            root_value = self._heap[0]
            self._heap[0] = self._heap[-1]
            self._heap.pop(-1)
            self._downheap(0)
            return root_value
        else:
            raise RuntimeError('Heap empty')

    def _downheap(self, index):
        #Define a recursive downheap
        #Make sure to check for how many
        #children a given index has
        #HINT: You use the min(val1, val2)
