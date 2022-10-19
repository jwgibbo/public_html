#binarytree.py
from bnode import BNode

class BinaryTree:
    def __init__(self):
        self._root = None

    def add(self, entry):
        #Assume beautiful working
        #definition here

    #Public facing method
    def is_in(self, target):
        return self._rec_is_in(self, target, self._root)

    #Hidden recursive method
    def _rec_is_in(self, target, cur_node):
        #base case #1: cur_node == None
        #base case #2: entry in cur_node == target
        #recursive case: look in both LST and RST
        
