#binarysearchtree.py

from binarynode import BinaryNode

class BinarySearchTree:
    def __init__(self):
        self._root = None

    def search(self, search_key):
        """Retrieve ItemType object"""
        return _rec_search(self, search_key, self._root)

    def _rec_search(self, search_key, cur_node):
        #Board work: define this to either return
        #object that matches the key OR raise KeyError
