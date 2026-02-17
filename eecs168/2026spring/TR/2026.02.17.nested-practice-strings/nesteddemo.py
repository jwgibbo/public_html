for row in range(4):
    print(row, '| ', end='')
    for col in range(5):
        print(col, end=' ')
    print('')

print('----------------')

for row in range(4):
    for col in range(5):
        if row==2 and col==3:
            print('?', end='')
        else:
            print('$', end='')
    print('') #newline
