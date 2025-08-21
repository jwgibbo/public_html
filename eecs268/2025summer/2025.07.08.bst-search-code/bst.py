#bst.py

from binarynode import BinaryNode

class BST:
    def __init__(self):
        self._root = None

    def add(self, item):
        self._rec_add(item, self._root)

    def _rec_add(self, item, cur_node):
        if cur_node is None:
            cur_node = BinaryNode(item)

    def search(self, key):
        return self.rec_search(key, self._root)

    def _rec_search(self, key, cur_node):
        #define this (Tuesday)
        
