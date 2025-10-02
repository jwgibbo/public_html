grid = []

#Goal: 10 rows of 5 42s in grid
#      
ROWS = 10
COLS = 5
for row_num in range(ROWS):
    empty_list = []
    grid.append(empty_list)
    for col_num in range(COLS):
        grid[row_num].append(42)

#Print all the lists in grid
for row in grid:
    print(row)

print('--------')

#Print all the values but using indices
for row_num in range(ROWS):
    for col_num in range(COLS):
        print(grid[row_num][col_num], end=' ')
    print('')
