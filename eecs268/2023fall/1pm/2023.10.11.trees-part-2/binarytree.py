#binarytree.py

from binarynode import BinaryNode

class BinaryTree:
    def __init__(self):
        self._root = None

    #Assume we have a working
    #add method

    def search(self, target):
        return self._rec_search(target, self._root)

    def _rec_search(self, target, cur_node):
        #define this

    def count_nodes(self):
        return self._rec_count_nodes(self._root)

    def _rec_count_nodes(self, cur_node):
        #define this
        
        
