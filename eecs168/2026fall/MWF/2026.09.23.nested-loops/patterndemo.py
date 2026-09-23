# Goal: print a grid of 3 rows of 5
#       $'s each
rows = 3
cols = 5
for row in range(rows):
    for col in range(cols):
        print('$', end='')

    print('') #newline between rows
