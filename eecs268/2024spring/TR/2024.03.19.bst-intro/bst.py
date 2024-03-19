#bst.py
from binarynode import BinaryNode
class BST:
    def __init__(self):
        self._root = None

    def add(self, entry):
        #public facing, non-recursive
        if self._root is None:
            self._root = BinaryNode(entry)
        else:
            self._rec_add(entry, self._root)

    def _rec_add(self, entry, cur_node):
        #hidden, recursive
        if entry < cur_node.entry:
            if cur_node.left is None:
                #add it!
            else:
                self._rec_add(entry, cur_node.left)
        #finish this definition for board work
