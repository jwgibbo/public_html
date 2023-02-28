grid = [[2,4,6,8], [3,6,9,12], [4,8,12,16]]

for row in grid:
    for num in row:
        print(num, end=' ')

    #still in the outer loop
    #but a row has been printed
    print('\n', end='')
