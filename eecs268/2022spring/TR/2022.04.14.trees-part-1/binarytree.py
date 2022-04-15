#binarytree.py

class BinaryTree:
    def __init__(self):
        self._root = None

    def add(self, entry):
        #assume this works

    def search(self, target):
        return self._rec_search(target, self._root)

    def _rec_search(self, target, cur_node):
        #You will define
        #Find your base cases first!
        #Deal with cur_node being None first
        
