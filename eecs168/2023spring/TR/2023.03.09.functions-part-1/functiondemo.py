#Goal: Define a function that takes a
#      number and returns that number
#      plus one
def plus_one(num):
    answer = num + 1
    return answer


#Make a call to plus_one
print(plus_one(5))

#If a function returns a value
#you can use that value anywhere
#that type is normally used
result = plus_one(54) + plus_one(2)
print(result)
