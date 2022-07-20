#bst.py

from bnode import BNode


class BST:
    def __init__(self):
        self._root = None

    def search(self, search_key):
        return(self._rec_search(search_key, self._root))

    def _rec_search(self, search_key, cur_node):
        #Board work
        #Raise a RuntimeError if search fails

    def add(self, entry):
        self._rec_add(entry, self._root)

    def _rec_add(self, entry, cur_node):
        #if current subtree is empty
        if cur_node == None:
            cur_node = BNode(entry)
        #elif check to see if it's a duplicate
        #elif check to see if we go left or right
            
