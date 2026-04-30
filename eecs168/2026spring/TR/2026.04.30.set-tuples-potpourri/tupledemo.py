#tupledemo.py

def main():
    my_tup = (10, 5, 20, 55)
    print(len(my_tup))
    print(my_tup)
    print(my_tup[2])
    # my_tup[2] = -1 ERROR

    sample_tup = ('wall-e', 10)
    title, rating = sample_tup
    print(title)
    print(rating)
    my_tup = my_tup + (5, 25)
    print(my_tup)

main()
