#binarytree.py

from binarynode import BinaryNode

class BinaryTree:
    def __init__(self):
        self._root = None

    def add(self, entry):
        pass #for now assume this works

    def search(self, target):
        return self._rec_search(target, self._root)

    def _rec_search(self, target, cur_node):
        if cur_node is None:
            return False
        elif cur_node.entry == target:
            return True
        else:
            
            #otherwise search the LST and RST
        
        
