
#Consider the following code

#The number of instructions is constant
num = 0
while num < 10:
    print(num)
    num += 1

print('=======')

#This algorithm scales linearly
num = 0
upper = int(input("Enter an upper bound: "))
while num < upper:
    print(num)
    num += 1

print('=======')
#This scale quadratic, specifically
#n^2
n = 1000
for i in range(n):
    for j in range(n):
        print(i+j)
