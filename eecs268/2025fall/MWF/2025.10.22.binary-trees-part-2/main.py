#main.py

from binarytree import BinaryTree

def main():
    my_tree = BinaryTree()
    my_tree.add('A')
    my_tree.add('B')
    my_tree.add('C')
    my_tree.add('D')

    if my_tree.search('C'):
        print('C is in the tree')
    else:
        print('C is NOT in the tree')
