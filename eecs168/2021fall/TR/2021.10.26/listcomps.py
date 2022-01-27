def main():
    nums = [-5, 10, 15, -20, 25]

    #Goal: Create a new list that
    #       contains only the
    #       positive values in nums
    positives = [num for num in nums if num > 0]

    #Goal: Create a new list that
    #       contains the squares of all
    #       values from nums
    squares = [num for num in nums]
    
    print(positives)
    print(squares)

main()
