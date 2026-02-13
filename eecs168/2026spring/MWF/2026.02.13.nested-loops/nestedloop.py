print('outer\tinner')
print('-------------')
for outer in range(1, 4):
    for inner in range(12, 15):
        print(outer, '\t', inner)

    print('Inner loop finished')

    
print('----------')
#Goal: Print a grid of numbers
for outer in range(3):
    print(outer, '| ', end='')
    for inner in range(1, 5):
        print(inner, end=' ')

    print('') #newline after each row


        
#Goal: Print a grid of $'s
print('----------')
for row in range(3):
    for col in range(4):
        print('$', end='')
    print('')
