print('outer\tinner')

for outer in range(1, 4):
    for inner in range(10, 14):
        print(f'{outer}\t{inner}')

    print('inner loop finished')
