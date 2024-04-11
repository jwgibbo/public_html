
for num in range(10):
    #do something
    pass

#n is our problem size
#This algorithm scales linearly
n = 100000
for num in range(n):
    #do something
    pass
print('first one done')


#This one scale quadratically
for i in range(n):
    for j in range(n):
        #do something
        pass
print('second one done')
