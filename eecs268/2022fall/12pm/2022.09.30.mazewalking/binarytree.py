#binarytree.py
from bnode import BNode
class BinaryTree:
    def __init__(self):
        self._root = None

    #Assume this works
    def add(self, entry):
        #Awesome, bugfree, definition

    #public facing method
    def is_in(self, target):
        return self._rec_is_in(self, target, self._root)

    def _rec_is_in(self, target, cur_node):
        #recursive helper method
        #Base case: cur_node == None
        #Recursive case: check LST and check RST
        
