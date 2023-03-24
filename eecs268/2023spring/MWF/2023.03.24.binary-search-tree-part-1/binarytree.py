#binarytree.py

from binarynode import BinaryNode

class BinaryTree:
    def __init__(self):
        self._root = None

    def add(self, entry):
        #Assume this works

    def search(self, target):
        return self.rec_search(target, self._root)

    def _rec_search(self, target, cur_node):
        #hidden/"private" recursive method
        if cur_node == None:
            return False
        elif cur_node.entry == target:
            return True
        else:
            #recursive case by searching LST and RST
