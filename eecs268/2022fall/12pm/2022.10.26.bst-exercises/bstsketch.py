#binarysearchtree.py

from bnode import BNode

class BinarySearchTree:
    def __init__(self):
        self._root = None

    def search(self, key):
        return self._rec_search(self, key, self._root)

    def _rec_search(self, key, cur_node):
        #Base 1: cur_node = None, raise exception
        #Base 2: cur_node contains object matching key
        #        return the entry
        #Recursive case: Decide to go LST or RST by comparing
        #                 entry to the key

    def add(self, entry):
        self._rec_add(self, entry, self._root)

    def _rec_add(self, entry, cur_node):
        if cur_node == None:
            cur_node = BNode(entry)
    
