#main.py

from node import Node

def main():
    front = Node('A')
    front.next = Node('B')
    front.next.next = Node('K')


main()
