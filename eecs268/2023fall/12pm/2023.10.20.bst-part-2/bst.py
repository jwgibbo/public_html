#bst.py

from binarynode import BinaryNode

class BST:
    def __init__(self):
        self._root = None

    def search(self, key):
        return self._rec_search(key, self._root)

    def _rec_search(self, key, cur_node):
        if cur_node is None:
            raise RuntimeError
        elif cur_node.entry == key:
            return cur_node.entry
        elif cur_node.entry < key:
            return self._rec_search(target, cur_node.right)
        else:
            return self._rec_search(target, cur_node.left)

    def add(self, item):
        if self._root is None:
            self._root = BinaryNode(item)
        else:
            self._rec_add(item, self._root)

    def _rec_add(self, item, cur_node):
        #This method assume cur_node is always a node

    
