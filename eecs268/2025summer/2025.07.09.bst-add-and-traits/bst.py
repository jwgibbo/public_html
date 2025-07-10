#bst.py

from binarynode import BinaryNode

class BST:
    def __init__(self):
        self._root = None

    def add(self, item):
        #check if entire tree is empty
        if self._root is None:
            self._root = BinaryNode(item)
        else:
            #cur_node is looking at a node
            self._rec_add(item, self._root)

    def _rec_add(self, item, cur_node):
        #cur_node will never become None;
        #it will always be referrencing a BinaryNode
        

    def search(self, key):
        return self.rec_search(key, self._root)

    def _rec_search(self, key, cur_node):
        #define this (Tuesday)
        
