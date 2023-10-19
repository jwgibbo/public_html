#bst.py

from binarynode import BinaryNode

class BST:
    def __init__(self):
        self._root = None

    def search(self, target):
        return self._rec_search(target, self._root)

    def _rec_search(self, target, cur_node):
        #define this to either return the
        #entry of the node that matches the target
        #or raise a RuntimeError
