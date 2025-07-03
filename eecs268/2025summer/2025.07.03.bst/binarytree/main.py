#main.py

from binarytree import BinaryTree

def main():
    my_tree = BinaryTree()
    my_tree.add('A')
    my_tree.add('B')
    my_tree.add('C')
    my_tree.add('D')
    my_tree.add('E')
    my_tree.add('F')

    if my_tree.search('F'):
        print('It is in there!')
    else:
        print('Not found')

    print(my_tree.count_nodes()) #prints 6
