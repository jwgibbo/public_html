#bst.py

from binarynode import BinaryNode

class BST:
    def __init__(self):
        self._root = None

    def search(self, key):
        return self._rec_search(key, self._root)

    def _rec_search(self, key, cur_node):
        #define this Monday Mar 30th

    def add(self, entry):
        if self._root is None:
            self._root = BinaryNode(entry)
        else:
            self._rec_add(entry, self._root)

    def _rec_add(self, entry, cur_node):
        #define this Wed Apr 1st
        
'''OLD BUSTED VERSION
    def add(self, entry):
        self._rec_add(entry, self._root)

    def _rec_add(self, entry, cur_node):
        if cur_node is None:
            cur_node = BinaryNode(entry)
'''
