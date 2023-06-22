#linkedlist.py

from node import Node

class LinkedList:
    def __init__(self):
        self._front = None
        self._length = 0

    def insert(self, index, entry):
        if index < 0 or index > self._length:
            raise IndexError
        elif index == 0:
            new_node = Node(entry)
            new_node.next = self._front
            self._front = new_node
            self._length += 1
        else:
            new_node = Node(entry)
            previous = self._front

            #move previous to the index
            #before the insert point
            for i in range(index-1):
                previous = prevous.next

            #Might be a node or None
            #Either is fine
            target = previous.next

            #insert the node
            previous.next = new_node
            new_node = target
            self._length += 1
