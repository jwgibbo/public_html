
#Constant, O(1)
for num in range(9999):
    #do something
    pass
print('Constant loop finished')

n = 100000

#Scaling linearly with n, O(n)
for num in range(n):
    #do something
    pass
print('Linear loop finished')
print('Reminder: CTRL+C kills a program if you get impatient')

#Scaling quadratically, O(n^2)
for i in range(n):
    for j in range(n):
        #do something
        pass
print('quadratic loop finished')
