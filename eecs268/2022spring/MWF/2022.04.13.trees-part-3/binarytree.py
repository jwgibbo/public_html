from bnode import BNode

class BinaryTree:
    def __init__(self):
        self._root = None

    def add(self, entry):
        #assume this works
        #we'll define a formal
        #add when we get to BST
    
    def search(self, target):
        return self._rec_search(target, self._root)

    def _rec_search(self, target, cur_node):
        #You will define this
        #Hint: Remember to identify bases cases!
        #Example if cur_node is None what do you do?
        #Hint 2: Return a bool
        #Hint 3: Let the recursion do some lifting

    def count(self, target):
        return self._rec_count(target, self._root)

    def _rec_count(self, target, cur_node):
        if cur_node == None:
            return 0
        else:
            lst_count = self._rec_count(target, cur_node.left)
            rst_count = self._rec_count(target, cur_node.right)
            if cur_node.entry == target:
                return 1 + lst_count + rst_count
            else:
                return lst_count + rst_count

    # Board work: define the two methods (public facing and
    # recursive helper method) that returns a count of leaves
    

    
