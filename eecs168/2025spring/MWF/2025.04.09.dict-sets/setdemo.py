def main():
    my_set = {'cat', 'john', 'pinball'}
    my_list = list() #empty
    
    print(my_set)
    print(my_list)

    my_set.add('dog')
    my_set.add('bat')
    my_set.add('pinball')
    print(my_set)
    #print(my_set[0])

    for elem in my_set:
        print(elem)

    print('----------')
    letters = set('banana')
    print(letters)

    words = ['the', 'apple', 'and', 'the', 'tree', 'are', 'happy', 'and', 'free']
    unique_words = set(words)
    print(unique_words)

    print('-----------')
    my_set = {1, 4, 9, 10, 7, 3}
    your_set = {2, 3, 5, 7, 1, 88}
    print(my_set.intersection(your_set))
    print(your_set.intersection(my_set))
    print(my_set.union(your_set))
    print(my_set.difference(your_set))
    print(your_set.difference(my_set))
    print(my_set.difference(my_set))
    

    

    


main()
