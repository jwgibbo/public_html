#Let's make a grid of numbers

grid = []

row1 = [5, 10, 15, 20]
row2 = [25, 30, 35, 40]
row3 = [45, 50, 55, 60]

grid.append(row1)
grid.append(row2)
grid.append(row3)

#For fun, assign all value to -1
for row_index in range(len(grid)):
    for col_index in range(len(grid[row_index])):
        print('Editing grid[', row_index, '][', col_index,']')
        grid[row_index][col_index] = -1
        
for row in grid:
    for num in row:
        print(num)
        
