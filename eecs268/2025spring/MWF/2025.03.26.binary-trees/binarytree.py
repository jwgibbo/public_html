#binarytree.py

from binarynode import BinaryNode

class BinaryTree:
    def __init__(self):
        self._root = None

    def add(self, entry):
        pass
        #we'll assume this works for now

    def search(self, target):
        return self._rec_search(target, self._root)

    def _rec_search(self, target, cur_node):
        if cur_node is None:
            return False
        elif cur_node.entry == target:
            return True
        else:
            #search the LST and RST
            is_in_LST = self._rec_search(target, cur_node.left)
            is_in_RST = self._rec_search(target, cur_node.right)
            return is_in_LST or is_in_RST

    
