#Make a loop that runs 10 times

for num in range(1000):
    print(num)


#This loop runs n times
#The time complexity scales with n
#in a linear way
n = ???
for num in range(n):
    print(num)

#This nested loop runs n**2 times
#This loop scales with n in
#a quadratic way
n = ???
for i in range(n):
    for j in range(n):
        print(f'i={i}\tj={j}')

#This loop scales in an n**3 way
n = ???
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(f'i={i}\tj={j}\tk={k}')
