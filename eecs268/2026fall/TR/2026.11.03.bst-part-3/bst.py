#bst.py
from binarynode import BinaryNode

class BST:
    def __init__(self):
        self._root = None

    def add(self, item):
        if self._root is None:
            self._root = BinaryNode(item)
        else:
            self._rec_add(item, self._root)

    def _rec_add(self, item, cur_node):
        #define Today (Tuesday Nov 3)

''' OLD VERSION
    def _rec_add(item, cur_node):
        if cur_node is None:
            cur_node = BinaryNode(item)
'''

    def search(self, target):
        return self._rec_search(target, self._root)

    def _rec_search(self, key, cur_node):
        if cur_node is None:
            return False
        elif cur_node.entry == key:
            return True
        elif cur_node.entry > key:
            return self._rec_search(key, cur_node.left)
        else:
            return self._rec_search(key, cur_node.right)
        
        
