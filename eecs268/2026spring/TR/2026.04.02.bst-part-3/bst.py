#bst.py

from binarynode import BinaryNode

class BST:
    def __init__(self):
        self._root = None

    def search(self, key):
        return self._rec_search(key, self._root)

    def _rec_search(self, key, cur_node):
        #define this (Tue Mar 31)


    def add(self, entry):
        if self._root is None:
            self._root = BinaryNode(entry)
        else:
            self._rec_add(entry, self._root)

    def _rec_add(self, entry, cur_node):
        #define this (Tue Mar 31)

''' OLD BUSTED VERSIONS 
    def add(self, entry):
        self._rec_add(entry, self._root)

    def _rec_add(self, entry, cur_node):
        if cur_node is None:
            cur_node = BinaryNode(entry)

'''
        
