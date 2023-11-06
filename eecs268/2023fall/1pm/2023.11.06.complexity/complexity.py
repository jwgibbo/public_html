#complexitydemo

#This runs with a constant
#  number of iterations
for num in range(10):
    print(num)
    
print('============')

#This scales linearly
n = int(input('Enter an n: '))
for num in range(n):
    print(num)

#This scales quadratically
n = int(input('Enter an n: '))
for i in range(n):
    for j in range(n):
        print(f'i={i}\tj={j}')
