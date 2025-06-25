#Goal: Make a 3x4 grid of numbers

row1 = [10, 20, 30, 40]
row2 = [11, 22, 33, 44]
row3 = [15, 25, 35, 45]

grid = [] #empty list
print(type(grid))
print(type(row1))

grid.append(row1)
grid.append(row2)
grid.append(row3)
print(grid)
print(type(grid))
print(type(grid[0]))
print(type(grid[0][0]))
