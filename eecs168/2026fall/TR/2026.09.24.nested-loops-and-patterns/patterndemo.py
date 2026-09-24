#Goal: Print 3x5 grid of *'s

num_rows = 3
num_cols = 5

for row in range(num_rows):
    for col in range(num_cols):
        print('*', end='')

    #print a newline
    print('')
