for outer in range(5):
    for inner in range(4):
        print(f'outer = {outer}\tinner = {inner}')
    
print('===========')

#Goal: Print the 0123 in a grid
#Example:
# 0123
# 0123
# 0123
# 0123
# 0123
for outer in range(5):
    for inner in range(4):
        print(inner, end='')

    #After each row, print a newline
    print('', end='\n')
    
    
