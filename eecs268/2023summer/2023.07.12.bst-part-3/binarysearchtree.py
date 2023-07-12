#binarysearchtree.py

from binarynode import BinaryNode

class BinarySearchTree:
    def __init__(self):
        self._root = None

    def add(self, item):
        if self._root == None:
            self._root = BinaryNode(item)
        else:
            self._rec_add(item, self._root)

    def _rec_add(self, item, cur_node):
        #define this
        #cur_node will always be looking at a node
        #raise a ValueError is for duplicates
        

    def search(self, target_key):
        #define

    def _rec_search(self, ???):
        #define
        
