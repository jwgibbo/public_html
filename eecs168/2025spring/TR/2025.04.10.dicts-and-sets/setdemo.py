def main():
    my_set = set()
    my_set.add('dog')
    my_set.add('dog')
    my_set.add('fish')
    print(my_set)
    my_set.add('cow')
    my_set.add('snake')
    my_set.add('bird')
    print(my_set)
    #print(my_set[0]) ERROR

    print('----------')
    my_set = {3, 8, 55, 14, 21, 6}
    your_set = {2, 6, 10, 8, 14, 33, 54}
    print(my_set.intersection(your_set))
    print(my_set.union(your_set))
    print(my_set.difference(your_set))
    print(your_set.difference(my_set))

    word = 'banana'
    letters = set(word)
    print(letters)
main()
