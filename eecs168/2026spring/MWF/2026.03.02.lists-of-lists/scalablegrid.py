#Goal: Create a grid with 3 rows and 5 cols
#   Let the user enter the numbers

grid = []

#How could we automate the creation of a row
for row_num in range(3):
    row = []
    for col_num in range(5):
        user_num = int(input("Enter a number: "))
        row.append(user_num)

    grid.append(row)

print(row)
print(grid)
