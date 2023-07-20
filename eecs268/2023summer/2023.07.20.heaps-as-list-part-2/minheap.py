#minheap

class MinHeap:
    def __init__(self):
        self._heap_list = []

    def add(self, entry):
        #add the entry to a spot that
        #keeps the heap complete
        self._heap_list.append(entry)

        #upheap the newly added value
        self._upheap(len(self._heap_list)-1)

    def _upheap(self, index):
        #define recursively 
    
