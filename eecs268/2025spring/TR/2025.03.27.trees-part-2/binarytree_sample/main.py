#main.py

from binarytree import BinaryTree

def main():
    my_tree = BinaryTree() #empty tree

    my_tree.add('A')
    my_tree.add('B')
    
    if my_tree.search('B'):
        print('B was found')
    else:
        print('B not found')
