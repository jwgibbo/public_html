grid = []

#Goal: Put three empty "rows" in grid
for i in range(3):
    empty_list = []
    grid.append(empty_list)

#Fill every row with five 99s
for row in grid:
    for i in range(5):
        row.append(99)

for row in grid:
    for num in row:
        print(num, ' ', end='')
    print('')
