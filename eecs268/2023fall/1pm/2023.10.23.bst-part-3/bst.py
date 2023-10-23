#bst.py

from binarynode import BinaryNode

class BST:
    def __init__(self):
        self._root = None

    def search(self, key):
        return self._rec_search(key, self._root)

    def _rec_search(self, key, cur_node):
        if cur_node is None:
            raise KeyError
        elif cur_node.entry == key:
            return cur_node.entry
        elif cur_node.entry > key:
            return self._rec_search(key, cur_node.left)
        elif cur_node.entry < key:
            return self._rec_search(key, cur_node.right)

    def add(self, entry):
        if self._root is None:
            self._root = BinaryNode(entry)
        else:
            self._rec_add(entry, self._root)

    def _rec_add(self, entry, cur_node):
        #cur_node will always refer to a BinaryNode
