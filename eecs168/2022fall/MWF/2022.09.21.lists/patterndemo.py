print('hello', end='!\n')
print('quiet!')


#Goal: print the following pattern:
'''
12345
12345
12345
'''

num_rows = 3
num_cols = 5
for row in range(num_rows):
    for col in range(1, num_cols+1):
        print(col, end='')
    #Still inside outer loop
    print('')#Get a newline by default
        
