print('outer\tinner')
for outer in range(1, 4):
    print('Inner loop starting.')
    for inner in range(10, 14):
        print(f'{outer}\t{inner}')
    print('Inner loop ending')

