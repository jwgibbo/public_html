def sum_positives(nums):
    total = 0
    for num in nums:
        total += num
    return total


def main():
    nums = [5,-10,15,-20,30,55]
    print( sum_positives(nums) )


if __name__ == "__main__":
    #call main in the global scope
    main()
