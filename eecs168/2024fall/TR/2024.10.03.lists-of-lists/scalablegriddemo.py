grid = []
#Now let's put 207 empty lists (rows) into 
#the grid
NUM_ROWS = 3
NUM_COLS = 5
for num in range(NUM_ROWS):
    grid.append( [] ) #adds empty list

#fill rows with 103 5's
for row in grid:
    for num in range(NUM_COLS):
        row.append(5)

print(grid)
