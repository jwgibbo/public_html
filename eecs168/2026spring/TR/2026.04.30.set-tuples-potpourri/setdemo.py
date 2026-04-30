#setdemo.py

def main():
    word1 = 'PIZZA'
    word2 = 'ZOOP'

    my_set = set(word1)
    your_set = set(word2)
    print(my_set)
    print(your_set)
    print('intersection: ', end='')
    print(my_set.intersection(your_set))


    print('union: ', end='')
    print(my_set.union(your_set))

    print('my_set difference your_set: ', end='')
    print(my_set.difference(your_set))

    print('your_set difference my_set: ', end='')
    print(your_set.difference(my_set))
    
    my_set.add('Q')
    print(my_set)

    print('-----')
    for letter in my_set:
        print(letter)


main()
