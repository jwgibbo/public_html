#main.py
from stack import Stack

def is_balanced(sequence):
    the_stack = Stack()

    for paren in sequence:
        if paren == '(':
            the_stack.push(paren)
        if paren == ')':
            if the_stack.is_empty():
                return False
            else:
                the_stack.pop()

    return the_stack.is_empty()
        
    
