#main.py

from node import Node

def main():
    first = Node(5)
    temp = Node(2)
    first.next = temp
    print(first.next.entry)

main()
