row1 = [10, 20, 30, 40]
row2 = [50, 60, 70, 80]
row3 = [90, 95, 99, 100]

grid = []
grid.append(row1)
print(grid)
print(len(grid))
grid.append(row2)
grid.append(row3)
print(grid)
print(len(grid))
print(type(grid))
print(type(grid[0]))
print(type(grid[0][0]))
print(grid[1][2])

for row in grid:
    for num in row:
        print(num, end=' ')
    print('')
