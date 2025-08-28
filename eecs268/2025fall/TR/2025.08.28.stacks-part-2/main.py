#main.py

from stack import Stack

def main():
    my_stack = Stack()
    my_stack.push(5)
    my_stack.push(10)
    my_stack.push(15)
    print(my_stack.peek())#15
    print(my_stack.pop()) #15
    print(my_stack.pop()) #10


