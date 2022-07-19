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
