#binarytree.py
from binarynode import BinaryNode

class BinaryTree:
    def __init__(self):
        self._root = None

    def add(self, entry):
        #assume this works for now

    def search(self, target):
        return self._rec_search(target, self._root)

    def _rec_search(self, target, cur_node):
        #what if cur_node is None
        #How do I look for a match?
        #Where do I look if I don't find it here
