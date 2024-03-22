#bst.py

from binarynode import BinaryNode

class BST:
    def __init__(self):
        self._root = None

    def add(self, entry):
        #Call a "private/hidden" recursive
        #method
        if self._root is None:
            self._root = BinaryNode(entry)
        else:
            self._rec_add(entry, self._root)

    def _rec_add(self, entry, cur_node):
        #recursive traverse through the tree
        #to find a spot to put a new node with
        #the new value OR raise a ValueError
        #if the value is a duplicate
        if entry < cur_node.entry:
            #Add it if the LST is empty
            #Otherwise, recurse into LST

    def search(self, key):
        #define

    def _rec_search(self, key, cur_node):
        #define
        
