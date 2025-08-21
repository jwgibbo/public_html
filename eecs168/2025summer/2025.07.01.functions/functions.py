#Goal: Define a function that takes in a number
#       and returns one more than that number

#=======================
def plus_one(num):
    answer = num + 1
    return answer
#=======================

result = plus_one(5)
print(result)
print(plus_one(99))
print(2*plus_one(3) + plus_one(5)*plus_one(1))
