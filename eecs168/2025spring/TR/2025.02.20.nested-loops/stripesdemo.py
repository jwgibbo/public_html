#Goal of printing a 5x5 grid of the following...
'''
ABABA
ABABA
ABABA
ABABA
ABABA
'''

num_rows = 5
num_cols = 5

for row in range(num_rows):
    for col in range(num_cols):
        if col%2 == 0:
            print('A', end='')
        else:
            print('B', end='')
    print('')
