
#Complexity O(1)
#constant time complexity
for num in range(10000):
    #do something
    pass


n = 1_000

#scaling in a linear way
#complexity O(n)
for num in range(n):
    #do something
    pass

print('O(n) loop done')

#scaling in a quadratic way
#complexity O(n^2)
for i in range(n):
    for j in range(n):
        #do something
        pass

print('O(n^2) loop done')

#This has a complexity of O(n^3)
for i in range(n):
    for j in range(n):
        for k in range(n):
            #do something
            pass
print('O(n^3) loop done')
