#Make a grid of 3 rows with 4 numbers each

grid = []

grid.append([1, 2, 3, 4])
grid.append([2, 4, 6, 8])
grid.append([3, 6, 9, 12])

print(grid)
print(len(grid))
print(grid[0])
print(type(grid[0]))
print(len(grid[0]))
print(grid[1][2])
print(type(grid[1][2]))

for row in grid:
    print(row)

print('------')

for row in grid:
    for num in row:
        print(num, end=' ')
    print('')
    
