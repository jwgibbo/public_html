#main.py

from binarytree from BinaryTree

#let us pretend our BinaryTree works

def main():
    my_tree = BinaryTree() #empty tree
    my_tree.add(5)
    my_tree.add(10)
    my_tree.add(15)

    if my_tree.search(10):
        print('10 is in there!')
    else:
        print('10 not found')

    print(my_tree.node_count()) #prints 3
