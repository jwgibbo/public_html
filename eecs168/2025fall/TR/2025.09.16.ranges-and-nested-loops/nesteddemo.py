print('outer\tinner')
for outer_num in range(1, 4):
    print('Entered outer loop')
    for inner_num in range(10, 13):
        print(f'{outer_num}\t{inner_num}')
    print('Done with inner loop')
        
