#bst.py

from binarynode import BinaryNode

class BST:
    def __init__(self):
        self._root = None

    def add(self, item):
        pass

    def search(self, key):
        return self._rec_search(key, self._root)

    def _rec_search(self, key, cur_node):
        #define this for Friday 4/4
