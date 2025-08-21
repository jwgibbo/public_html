n = 1000

#Algo 1
#   Always has 10 iterations
#   Constant time complexity
for num in range(10):
    #do something
    pass

print('Algo 1 done')

#Algo 2
#   Number of iterations grow with n
#   If n increases by 10, so does the amount
#       of iterations
#   Linear time complexity

for num in range(n):
    #do something
    pass

print('Algo 2 done')

#Algo 3
#   Quadratic complexity
for i in range(n):
    for j in range(n):
        #do something
        pass

print('Algo 3 done')


#Algo 4
#   n^3 complexity
for i in range(n):
    for j in range(n):
        for k in range(n):
            #do something
            pass

print('Algo 4 done')
