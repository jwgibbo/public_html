#main.py

from node import Node

def main():
    first = Node('A')
    temp = Node('B')
    first.next = temp
    print(temp.entry)
    print(first.next.entry)
    temp.next = Node('C')
    print(first.next.next.entry)

main()
