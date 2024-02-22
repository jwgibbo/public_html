grid = []

row1 = [100, 200, 300, 400]
row2 = [5, 10, 15, 20]

grid.append(row1)
grid.append(row2)


print(len(grid))
print(type(grid[0]))
print(type(grid[0][1]))

grid[1][2] = 99
print(grid)
