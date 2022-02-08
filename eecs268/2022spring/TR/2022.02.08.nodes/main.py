def main():
    list1 = [1,2,3,4]
    list2 = [1,2,3,4]

    print(list1 == list2)
    print(list1 is list2)

    list2 = list1
    print(list1 == list2)
    print(list1 is list2)

if __name__ == "__main__":
    main()
