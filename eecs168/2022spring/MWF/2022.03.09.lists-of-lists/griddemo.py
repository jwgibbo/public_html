def main():
    grid = [[5, 10, 15], [20, 25, 30]]
    print(grid)
    print(grid[0])
    print(grid[1][2])

    #goal print all values
    #from the grid
    for row in grid:
        for col in row:
            print(col, end=' ')
        print('')

    #Lightning round!
    #Legal or Illegal?
    grid[0].append(99)
    print(grid)

    grid.append([55, 88, 77])
    print(grid)

    #grid[1][2].append(42) ERROR
    #print(grid)

    word_grid = [['bat', 'cat', 'hat'],
                 ['mat', 'ham', 'can'],
                 ['banana', 'galapagos']]
    print(word_grid)
    print(word_grid[1])
    print(word_grid[1][1].upper())
    print(word_grid[1][1][0])
main()
