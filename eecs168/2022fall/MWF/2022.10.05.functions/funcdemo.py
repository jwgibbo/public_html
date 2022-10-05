#Goal: Define a function that takes
#       a number and return that
#       number plus 1

def add_one(num):
    #Inside your definition
    #you can access the parameters
    #and locally declared variables
    ans = num + 1
    return ans

def doubler(num):
    return num*2

def double_doubler(num):
    ans = doubler(doubler(num))
    return ans

#Goal: Define a function that takes
#       a number and return True if
#       the number is odd, False otherwise
def is_odd(num):
    if num % 2 == 1:
        return True
    else:
        return False


user_num = int(input("Enter number: "))
result = add_one(user_num)
print(result)
result = doubler(user_num)
print(result)
result = double_doubler(user_num)
print(result)
print(add_one(doubler(1)))
