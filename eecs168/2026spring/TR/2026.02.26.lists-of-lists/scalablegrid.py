#Let's create 3 rows of 5 numbers from the user
grid = [] #make an empty grid
row = [] #make an empty row

for row_num in range(3):

    for col_num in range(5):
        user_input = int(input('Enter a number: '))
        row.append(user_input)

    grid.append(row)

print(grid)
