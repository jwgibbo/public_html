#bst.py
from binarynode import BinaryNode

class BST:
    def __init__(self):
        self._root = None

    def add(self, entry):
        pass #until Tuesday

    def search(self, target):
        return self._rec_search(target, self._root)

    def _rec_search(self, target, cur_node):
        if cur_node is None:
            return False
        elif cur_node.entry == target:
            return True
        elif cur_node.entry > target:
            return self._rec_search(target, cur_node.left)
        else:
            return self._rec_search(target, cur_node.right)
        
        
