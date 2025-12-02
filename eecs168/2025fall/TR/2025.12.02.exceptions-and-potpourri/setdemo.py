def main():
    my_set = {'a', 'b', 'c', 'd'}
    your_set = {'e', 'f', 'a', 'd', 'g'}

    print(my_set.intersection(your_set))
    print(my_set.union(your_set))
    print(my_set.difference(your_set))
    print(your_set.difference(my_set))
    

main()
