#Goal: Define a function that takes in a
#       number and return one more than that
#       number
def plus_one(num):
    #don't need to do this...
    #num = int(input('enter a number')
    answer = num + 1
    #don't need to print answer
    return answer

result = plus_one(2)
print(result)

result = plus_one(5) + plus_one(99)
print(result)
