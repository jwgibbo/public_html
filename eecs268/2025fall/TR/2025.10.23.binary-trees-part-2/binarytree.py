#binarytree.py

from binarynode import BinaryNode

class BinaryTree:
    def __init__(self):
        self._root = None

    def add(self, entry):
        pass #assume this works

    def search(self, target):
        #return True if target is in tree
        return self._rec_search(target, self._root)

    def _rec_search(self, target, cur_node):
        if cur_node is None:
            return False
        elif cur_node.entry == target:
            return True
        #finish this definition to search LST and RST

    def node_count(self):
        return self._rec_node_count(self._root)

    def _rec_node_count(self, cur_node):
        #define this (Thur Oct 23)
