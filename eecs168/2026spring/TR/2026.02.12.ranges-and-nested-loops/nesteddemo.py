print('outer\tinner')
print('-------------')

for outer in range(1, 4):
    for inner in range(12, 17):
        print(outer, '\t', inner)

    print('Inner loop finished')

print('--------')

#Goal: print 3 rows with 5 $s each
for outer in range(5):
    for inner in range(15):
        print('$', end='')
    print('')#new line between rows



