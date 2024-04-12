#Constant complexity
#O(1)
for num in range(9999):
    #do something
    pass

#n is our problem size
#This algorithm scales linearly
# O(n)
n = 100000
for num in range(n):
    #do something
    pass
print('first one done')


#This one scale quadratically
# O(n^2)
for i in range(n):
    for j in range(n):
        #do something
        pass
print('second one done')
