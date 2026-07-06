#bst.py

from binarynode import BinaryNode

class BST:
    def __init__(self):
        self._root = None

    def add(self, entry):
        #We will define, I promise

    def search(self, target):
        return self._rec_search(target, self._root)

    def _rec_search(self, target, cur_node):
        if cur_node is None:
            raise KeyError('Target not found')
        elif cur_node.entry == target:
            return cur_node.entry
        elif target < cur_node.entry:
            return self._rec_search(target, cur_node.left)
        elif target > cur_node.entry:
            return self._rec_search(target. cur_node.right)
        
            
            
