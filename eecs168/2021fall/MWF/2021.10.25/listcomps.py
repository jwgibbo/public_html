def main():
    nums = [-5, 10, 15, -20, -30, 55]
    #Goal: Create a list that contains
    #all the positive values from nums
    positives = [num for num in nums if num > 0]

    #Goal: Create a list of all the
    #      square of each value from nums
    squares = [num**2 for num in nums]        
    print(positives)
    print(squares)


main()
