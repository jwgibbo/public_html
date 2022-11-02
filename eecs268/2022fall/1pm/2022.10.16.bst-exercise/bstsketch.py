#binarysearchtree.py


from bnode import BNode

class BinarySearchTree:
    def __init__(self):
        self._root = None

    def search(self, key):
        '''Hand back the object matching the key'''
        return self._rec_search(key, self._root)

    def _rec_search(self, key, cur_node):
        #Base case 1: cur_node == None, raise ValueError
        #Base case 2: cur_node contains a match, return entry
        #Recursive case: Decide to go LST or RST

    def add(self, entry):
        self._rec_add(entry, self.root)

    def _rec_add(self, entry, cur_node):
        #This won't help
        if cur_node == None:
            cur_node = Node(entry)
