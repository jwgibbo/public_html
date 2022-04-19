#bst.py

from bnode import BNode


class BST:
    def __init__(self):
        self._root = None

    #Assume an add works

    def search(self, key):
        return self._rec_search(self, key, self._root)

    def _rec_search(self, key, cur_node):
        #Assume that comparison operators are overloaded
        # Example:      cur_node.entry == key   is valid
        #               cur_node < key
        #               cur_node > key
        # If item is not in the tree, raise an exception
