#main.py

from binarytree import BinaryTree

def main():
    my_tree = BinaryTree()
    my_tree.add('zebra')
    my_tree.add('human')
    my_tree.add('gibbons')
    my_tree.add('john gibbons')

    if my_tree.is_in('zebra'):
        print("Go home zebra, you're drunk")
    else:
        print("Tree is zebra free")
    
