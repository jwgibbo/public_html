grid = []

row1 = [2, 4, 6, 8]
row2 = [3, 6, 9, 12]
row3 = [4, 8, 12, 16]

grid.append(row1)
print(grid)
print(f'grid length = {len(grid)}')
print(type(grid))
print(type(grid[0]))
print(grid[0][2])
print(type(grid[0][2]))

grid.append(row2)
grid.append(row3)
print(grid)
#print(grid[3][0])

#Let's iterate across the grid
for row in grid:
    for number in row:
        print(number, end=' ')
    print('')
