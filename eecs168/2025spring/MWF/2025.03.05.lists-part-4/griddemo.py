#griddemo.py
#Goal: Make a 3x4 "2D" list dynamically

grid = []
num_rows = 3
num_cols = 4
#append 3 empty lists to grid
for row in range(num_rows):
    grid.append([])
    
print(grid)
print(len(grid))

#Goal: fill each row with four 99s
for row in grid:
    for col in range(num_cols):
        #You could get user input here
        row.append(99)

print(grid)
