#binarytree.py
from bnode import BNode

class BinaryTree:
    def __init__(self):
        self._root = None

    def add(self, entry):
        #Assume beautiful working
        #definition here

    #Public facing method
    def is_in(self, target):
        return self._rec_is_in(self, target, self._root)

    #Hidden recursive method
    def _rec_is_in(self, target, cur_node):
        if cur_node == None:
            return False
        elif cur_node.entry == target:
            return True
        else:
            is_in_LST = self._rec_is_in(target, cur_node.left)
            is_in_RST = self._rec_is_in(target, cur_node.right
            return is_in_LST or is_in_RST
