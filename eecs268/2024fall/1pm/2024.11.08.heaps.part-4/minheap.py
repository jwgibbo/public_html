#minheap.py

class MinHeap:
    def __init__(self):
        self._heap = [] #empty list/heap

    def add(self, entry):
        #add to the end of the list
        self._heap.append(entry)
        self._upheap(len(self._heap)-1)

    def _upheap(self, index):
        #define upheap as a board
        #do so recursively
        
    def remove(self):
        root_value = self._heap[0]

        #move the temp root into index zero
        self._heap[0] = self.heap[-1]
        self._heap.pop(-1)

        self._downheap(0)

        return root_value

    def _downheap(self, index):
        #define the downheap process for
        #the left child only case
        if _________:
            #fill this in
