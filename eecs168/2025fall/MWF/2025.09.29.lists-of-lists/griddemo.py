#Goal: Make a grid of numbers

row1 = [10, 20, 30, 35]
row2 = [40, 50, 60, 65]
row3 = [70, 80, 90, 95]

grid = []
grid.append(row1)
print(grid)
print(len(row1))
print(len(grid))
grid.append(row2)
grid.append(row3)
print(grid)
print(len(grid))
print(type(grid))
print(type(grid[0]))
print(grid[1][2])
print(type(grid[1][2]))
print(grid[2][2])
#print(grid[3][2])

for row in grid:
    for num in row:
        print(num, end=' ')
    print('')
    
