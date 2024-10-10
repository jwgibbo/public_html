#binarytree.py

from binarynode import BinaryNode

class BinaryTree:
    def __init__(self):
        self._root = None

    def add(self, entry):
        #Assume this work

    def search(self, target):
        #this is just a public facing method
        return self._rec_search(target, self._root)

    def _rec_search(self, target, cur_node):
        #recursively search for target
