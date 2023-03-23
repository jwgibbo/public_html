#binarytree.py
from binarynode import BinaryNode

class BinaryTree:
    def __init__(self):
        self._root = None

    def add(self, entry):
        #Assume this works

    def search(self, target):
        #This will be a "public
        #facing" method
        return self.rec_search(target, self._root)

    def rec_search(self, target, cur_node):
        if cur_node == None:
            return False
        elif cur_node.entry == target:
            return True
        else:
            #Recursive into LST and RST
            #If you find it either return True
            #If you don't find it at all return False
