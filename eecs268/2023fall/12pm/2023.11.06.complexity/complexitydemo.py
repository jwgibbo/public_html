#complexydemo.py

#This runs in constant time
for num in range(10):
    print(num)

print('=============')

#scales with n linearly
n = int(input('Enter an n: '))
for num in range(n):
    print(num)

print('=============')
#This is quadratic growth
n = int(input('Enter an n: '))
for i in range(n):
    for j in range(n):
        print(f'i={i}\tj={j}')
