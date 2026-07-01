#binarytree.py

from binarynode import BinaryNode

class BinaryTree:
    def __init__(self):
        self._root = None

    def add(self, entry):
        #Assume this works...for now

    def search(self, target):
        #returns True if the target is in the tree
        return self._rec_search(target, self._root)

    def node_count(self):
        return self._rec_node_count(self._root)

    def _rec_node_count(self, cur_node):
        #define this

    def _rec_search(self, target, cur_node):
        if cur_node is None:
            return False
        elif cur_node.entry == target:
            return True
        else:
            #look in the LST and RST of cur_node
            is_in_LST = self._rec_search(target, cur_node.left)
            is_in_RST = self._rec_search(target, cur_node.right)
            return is_in_LST or is_in_RST

    def print_all(self):
        self._rec_print(self._root)

    def _rec_print_all(self, cur_node):
        #define this
