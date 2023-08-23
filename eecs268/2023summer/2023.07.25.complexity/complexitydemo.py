#complexitydemo.py


#Constant time complexity
#There is n controls the number
#of instructions required
for num in range(10):
    #do something with num


#This algorithm scales with the
#problem size n in a linear way
n = ???
for num in range(n):
    #do something with num


#The time complexity of this nested
#loop is scaling with n in a quadratic way
n = ???
for i in range(n):
    for j in range(n):
        #do something with i and j

#Example of n^3 complexity
for i in range(n):
    for j in range(n):
        for k in range(n):
            #do something

#The space required by our list
#is scaling linearly with n
my_list = []
n = ???
for num in range(n):
    my_list.append(n)
