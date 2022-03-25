def main():
    #recall how to make a simple list
    nums = [5, 10, 15, 20]
    #see notes for visualization


    #Now let's make a list of lists
    grid = [ [2,4,6], [8,10,55], [14,16,18] ]
    #See notes for visualization


    print(type(grid))
    print(type(grid[1]))
    print(grid[1])
    print(type(grid[1][2]))
    print(grid[1][2])


    grid2 = [list(nums), list(nums), list(nums)]
    print(grid2)
    grid2[0][2] = 99
    print(grid2)
    print(nums)
    

main()
