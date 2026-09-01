#main.py

from node import Node

def main():
    first = Node('A')
    second = Node('B')
    first.next = second
    print(first.entry)
    print(second.entry)
    print(first.next.entry)

main()
