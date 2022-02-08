from node import Node

def main():
    front = Node(17)
    temp = Node(55)
    front.next = temp
    print(front.entry)
    print(type(front.next))
    print(front.next.entry)
    temp = Node(42)
    front.next.next = temp
    
    #Board work: create the sequence
    #in the notes without making any
    #more local variables in main
    
main()
