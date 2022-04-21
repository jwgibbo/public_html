#bst.py
from bnode import BNode

class BST:
    def __init__(self):
        self._root = None

    def search(self, key):
        return self._rec_search(key, self._root)

    #define _rec_search

    def add(self, entry):
        if self._root == None:
            self._root = BNode(entry)
        elif self._root.entry == entry:
            raise RuntimeError('No duplicates allowed!')
        else:
            self._rec_add(entry, self._root)

    def _rec_add(self, entry, cur_node):
        #define this
