def changer(the_list):
    the_list[0] = 99


def main():
    x = 14
    nums = [5, 10, 15, 20]
    print(nums)
    changer(nums)
    print(nums)

    list1 = [10, 20, 30]
    list2 = list1
    list2 = [44, 45, 46]
    list2[0] = 55
    print(list1)

    word1 = 'cats'
    word2 = word1
    word2 = 'dogs'
    print(word1)
    print(word2)


main()
