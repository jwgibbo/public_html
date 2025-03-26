#main.py

from binarytree import BinaryTree

def main():
    my_tree = BinaryTree()
    my_tree.add('A')
    my_tree.add('B')
    my_tree.add('C')

    if my_tree.search('B'):
        print('it is in the tree!')
