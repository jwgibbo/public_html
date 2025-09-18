#Goal: print 3 rows of 4 $'s each
num_rows = 3
num_cols = 4
for row in range(num_rows):
    for col in range(num_cols):
        print('$', end='')
    print('')
