#main.py

from linkedqueue import LinkedQueue

def main():
    my_queue = LinkedQueue()

    my_queue.enqueue('John')
    my_queue.enqueue('Susy')
    #Assume I've enqueue LOTS of
    #names. One of the names is 'VIP'
    #Finish main such that the names
    #in front of VIP move to the back
    #VIP is at the front of the queue
