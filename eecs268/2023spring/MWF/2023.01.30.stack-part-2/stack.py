from node import Node

class Stack:
    def __init__(self):
        self._top = None

    def push(self, entry):
        new_node = Node(entry)
        new_node.next = self._top
        self._top = new_node

    def pop(self):
        if not self.is_empty():
            current_top_value = self._top.entry
            self._top = self._top.next
            return current_top_value
        else:
            raise RuntimeError("Pop attempted on empty stack")

    def peek(self):
        ???

    def is_empty(self):
        if self._top == None:
            return True
        else:
            return False
