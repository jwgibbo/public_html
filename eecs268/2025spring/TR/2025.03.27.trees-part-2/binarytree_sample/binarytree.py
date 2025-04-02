#binarytree.py
from binarynode import BinaryNode

class BinaryTree:
    def __init__(self):
        self._root = None

    def add(self, entry):
        pass
        #Assume this works

    def search(self, target):
        #initial call to recursive search
        return self._rec_search(target, self._root)

    def _rec_search(self, target, cur_node):
        if cur_node is None:
            return False
        elif cur_node.entry == target:
            return True
        else:
            #Didn't find target, but not done looking
            is_in_LST = self._rec_search(target, cur_node.left)
            is_in_RST = self._rec_search(target, cur_node.right)
            return is_in_LST or is_in_RST

    def node_count(self):
        return self._rec_node_count(self, self._root)

    def _rec_node_count(self, cur_node):
        #define for board work
    
        
