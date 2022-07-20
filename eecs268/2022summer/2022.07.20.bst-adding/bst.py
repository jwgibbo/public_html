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
        if self._root == None:
            self._root = BNode(entry)
        else:
            self._rec_add(entry, self._root)

    def _rec_add(self, entry, cur_node):
        #Our recursive add will always
        #be looking at a Node.
        #It will always stay one level "above"
        #None, so that we can edit the left
        #or right members of a Node
