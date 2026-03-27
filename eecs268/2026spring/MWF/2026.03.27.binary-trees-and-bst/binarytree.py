#binarytree.py

from binarynode import BinaryNode

class BinaryTree:
    def __init__(self):
        self._root = None

    def add(self, entry):
        pass
        #we'll assume this work (for now)

    def search(self, target):
        return self._rec_search(target, self._root)

    def _rec_search(self, target, cur_node):
        if cur_node is None:
            return False
        elif cur_node.entry == target:
            return True
        else:
            #define this (Wed)
            
    def node_count(self):
        return self._rec_node_count(self._root)

    def _rec_node_count(self, cur_node):
        #define this (Fri 2026.03.27)
