#bst.py

from binarynode import BinaryNode

class BST:
    def __init__(self):
        self._root = None

    def add(self, item):
        #we'll define this later

    def search(self, key):
        return self._rec_search(key, self._root)

    def _rec_search(self, key, cur_node):
        #define this
