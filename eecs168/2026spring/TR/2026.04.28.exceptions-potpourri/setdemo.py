#setdemo.py

def main():
    word1 = 'PIZZA'
    word2 = 'ZOOP'

    my_set = set(word1)
    your_set = set(word2)
    print(my_set)
    print(your_set)

    my_set.add('Q')
    print(my_set)

    print('-----')
    for letter in my_set:
        print(letter)

    print('intersection: ', end='')
    print(my_set.intersection(your_set))
main()
