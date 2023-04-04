#binarysearchtree.py

from binarynode import BinaryNode

class BinarySearchTree:

    def __init__(self):
        self._root = None

    def search(self, search_key):
        return self._rec_search(search_key, self._root)

    def _rec_search(self, search_key, cur_node):
        #Goal: Either return the object that
        #matches the key OR raise KeyError

    def add(self, item):
        self._rec_add(item. self._root)

    def _rec_add(self, item, cur_node)
        #WARNING WARNING! This does NOT change
        #self._root
        if cur_node == None:
            cur_node = BinaryNode(item)
