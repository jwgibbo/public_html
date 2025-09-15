#Goal: Use a nested loop to print
#       3 rows of 4 $'s each

#Can we just use a loop to print 4 &'s
for row in range(3):
    for col in range(4):
        print('$', end='')
    print('')
