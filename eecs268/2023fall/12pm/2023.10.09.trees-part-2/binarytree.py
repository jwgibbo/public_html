#binarytree.py

from binarynode import BinaryNode

class BinaryTree:
    def __init__(self):
        self._root = None

    def add(self, entry):
        #for now, assume this works

    def search(self, target):
        return self._rec_search(target, self._root)

    def _rec_search(self, target, cur_node):
        #do the recursive search
        
