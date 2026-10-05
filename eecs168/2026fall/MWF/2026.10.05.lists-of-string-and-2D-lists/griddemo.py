row1 = [3, 6, 9, 12]
row2 = [5, 10, 15, 20]
row3 = [7, 14, 21, 28]

grid = []

grid.append(row1)
grid.append(row2)
grid.append(row3)
print(len(grid))
print(type(grid))
print(type(grid[0]))
print(type(grid[0][0]))

for row in grid:
    for num in row:
        print(num)


print(grid[2][3])
print(grid[3][2])
