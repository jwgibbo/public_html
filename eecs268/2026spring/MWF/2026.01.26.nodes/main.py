#main.py

from node import Node

def main():
    first = Node('A')
    temp = Node('B')
    first.next = temp
    temp = Node('C')
    first.next.next = temp
    print(first.next.next)
    #finish coding main to match the drawing


main()
