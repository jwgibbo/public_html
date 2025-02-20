#patterndemo.py

#Goal: Print a 5x5 grid of + signs using nested loops
num_rows = 5
num_cols = 5

for row in range(num_rows):
    for col in range(num_cols):
        print('+', end='')

    #Code that only run as part of the outer loop
    #Here's where we can print a newline
    print('\n', end='')
    #OR print('', end='\n')
    #OR print('')
    #OR print()
