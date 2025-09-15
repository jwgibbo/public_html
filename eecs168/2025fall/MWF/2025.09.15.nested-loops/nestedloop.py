print('outer\tinner')

for outer_num in range(4):
    print('Entered outer loop')
    for inner_num in range(11, 15):
        print(f'{outer_num}\t{inner_num}')
    print('Finished inner loop')

print('Program over')
