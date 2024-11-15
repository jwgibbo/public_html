
for num in range(10):
    #do something
    pass
print('constant loop done')

n = 1_000_000

#grows linearly with n
for num in range(n):
    #do something
    pass
print('O(n) loop done')

#grows quadratically with n
for i in range(n):
    for j in range(n):
        #do something
        pass
print('O(n^2) loop done')

#Complexity of O(n^3)
for i in range(n):
    for j in range(n):
        for k in range(n):
            #do something
