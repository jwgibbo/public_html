#main.py

from node import Node

def main():
    first_node = Node("A")
    second_node = Node("B")

    first_node.next = second_node
