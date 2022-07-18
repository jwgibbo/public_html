#btree.py

class BinaryTree:
    def __init__(self):
        self._root = None

    def add(self, entry):
        #We'll assume this works


    def search(self, target):
        return self._rec_search(target, self._root)

    def _rec_search(self, target, cur_node):
        #Board work

    def node_count(self):
        return self._rec_node_count(self._root)

    def _rec_node_count(self, cur_node):
        '''Count all nodes'''
        
