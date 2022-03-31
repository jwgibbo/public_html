
#Consider the following loop

#The number of instructions this
#algorithm needs is constant
num = 0
while num < 10:
    print(num)
    num += 1

print('=====')

#The number of instructions this
#algorithms needs will scale with upper
#in linear way
num = 0
upper = int(input("Enter an upper bound: "))
while num < upper:
    print(num)
    num += 1

print('=====')
#This algorithm scales in a quadratic
#way, specifically n^2
num = 0
n = 100
for i in range(n):
    for j in range(n):
        print(num)
        num += 1


#Let's write a factorial function
def fact(num):
    if num <= 1:
        return 1
    else:
        return num * fact(num-1)
