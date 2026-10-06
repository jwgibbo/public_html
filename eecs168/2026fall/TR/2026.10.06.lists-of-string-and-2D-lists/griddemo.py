row1 = [2, 4, 6, 8]
row2 = [3, 6, 9, 12]
row3 = [4, 8, 12, 16]

print(len(row1))

grid = []
grid.append(row1)
grid.append(row2)
grid.append(row3)
print(len(grid))
print(type(grid))
print(type(grid[0]))
print(type(grid[0][0]))
print(grid[2][3])
# print(grid[3][2]) ERROR

for row in grid:
    for num in row:
        print(num)
    print('----')
