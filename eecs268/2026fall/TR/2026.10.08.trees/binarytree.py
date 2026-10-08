#binarytree.py
from binarynode import BinaryNode

class BinaryTree:
    def __init__(self):
        self._root = None

    def add(self, entry):
        pass #Assume this works for now

    def search(self, target):
        return self._rec_search(target, self.root)

    def _rec_search(self, target, cur_node):
        #This recurses through the tree
