#bst.py

from binarynode import BinaryNode


class BST:
    def __init__(self):
        self._root = None

    def add(self, item):
        if self._root is None:
            self._root = BinaryNode(item)
        else:
            self._rec_add(item, self._root)

    def _rec_add(self, item, cur_node):
        #Define on 4/8 (see notes)

    def search(self, key):
        return self._rec_search(key, self._root)

    def _rec_search(self, key, cur_node):
        #Return the item if found
        #or raise a KeyError if not found
