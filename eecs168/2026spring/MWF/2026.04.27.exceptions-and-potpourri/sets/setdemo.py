#setdemo.py

def main():
    word = 'BANANA'
    my_set = set(word)
    your_set = set('BABBLE')

    print('intersection: ', my_set.intersection(your_set))
    print('union: ', my_set.union(your_set))
    print('difference of my_set: ', my_set.difference(your_set))
    print('difference of your_set: ', your_set.difference(my_set))
    
    print(my_set)
    my_set.add('Z')
    print(my_set)
    my_set.add('A')
    print(my_set)
    my_set.remove('N')
    print(my_set)
    #my_set.remove('Q') ERROR


main()
