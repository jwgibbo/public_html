def main():
    my_set = {5, 15, 30, 36, 13}
    your_set = {20, 13, 10, 5, 8}

    print(my_set.intersection(your_set))
    print(my_set.union(your_set))
    print(my_set.difference(your_set))
    print(your_set.difference(my_set))

    print(my_set)
    my_set.add(99)
    print(my_set)
    my_set.remove(13)
    print(my_set)

main()
