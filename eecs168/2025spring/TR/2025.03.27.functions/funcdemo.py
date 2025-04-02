#Goal: Define a function that takes a number
#       and returns that number plus 1
def plus_one(num):
    answer = num + 1
    return answer

#We're outside the function definition
#Let's call the function
print( plus_one(4) )
print( plus_one(99) )
result = plus_one(9) + plus_one(29)
print(result)


for num in range(5):
    print(plus_one(num))
