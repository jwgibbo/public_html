
#Goal: Define a function that takes
#       a number and returns one more
#       than that number
def add_one(num):
    #ans is a locally declared variable
    ans = num + 1
    return ans

def doubler(num):
    ans = num*2
    return ans

def doubler_plus_one(num):
    ans = add_one(doubler(num))
    return ans

def is_odd(num):
    if num % 2 == 1:
        return True
    else:
        return False

def main():

    value = 5
    if is_odd(value) == True:
        print("It's odd!")
    else:
        print("It's not odd!")

    print(is_odd(value))

    result = doubler(2) + doubler(3)
    print(result)

main()
