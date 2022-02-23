#Goal: Define a function that takes a
#      number and returns that number
#      plus one

def add_one(num):
    #You can use all your tools
    #in a function definition
    answer = num + 1
    return answer

#Define a function that takes two
#numbers and returns the larger
def cool_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


my_num = 5

#the parameter num gets a value
#when we call add_one
one_more = add_one(my_num) #num = my_num
print(my_num)
print(one_more)
print(cool_max(3, 91))
