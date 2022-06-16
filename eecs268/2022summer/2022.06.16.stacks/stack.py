from node import Node

class Stack:
    def __init__(self):
        self._top = None #empty stack

    def is_empty(self):
        if self._top == None:
            return True
        else:
            return False

    def push(self, entry):
        #Create a Node and put entry in
        #the Node

        #Connect the new Node to the
        #current top

        #Move top to the new Node

    def pop(self):
        #if the stack isn't empty
            #Somehow keep a copy of the entry
            #at the top of the stack
            
            #move top to what is next
            #in the stack

            #return the value
        #otherwise raise exception

        
        
