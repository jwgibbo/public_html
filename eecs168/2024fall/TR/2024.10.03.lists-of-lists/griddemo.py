grid = []

row1 = [55, 65, 75, 85]
row2 = [56, 66, 76, 86]
row3 = [57, 67, 77, 87]

grid.append(row1)
grid.append(row2)
grid.append(row3)
print('length of grid =', len(grid))
print(grid)
print(grid[0])
print(grid[0][0])
print(grid[2][1])
print(grid[2][3])
#print(grid[3][2])

print('---------')
#Print each element of the grid,
#one at a time
for row in grid:
    for num in row:
        print(num, end=' ')
    print('')
        
