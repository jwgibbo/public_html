from node import Node


def main():
    first = Node(72)
    temp = Node(32)
    
    first.next = temp
    temp = Node(12)
    first.next.next = temp
    
    print(first.next.entry)
    print(first.next.next)
            
 

    
    

main()
