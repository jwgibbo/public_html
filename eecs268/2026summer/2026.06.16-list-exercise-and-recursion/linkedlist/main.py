#main.py

from linkedlist import LinkedList

def main():
    #Create an empty LinkedList
    my_list = LinkedList()

    my_list.insert(0, 'A')
    my_list.insert(1, 'B')
    my_list.insert(2, 'C')

    #print the entry at index 2
    print(my_list.get_entry(2)) #prints C

    #Our linked lists are NOT compatible with
    #for in loop like python lists!
    for index in range(my_list.length()):
        print(my_list.get_entry(index))

        #This prints A then B then C

    
