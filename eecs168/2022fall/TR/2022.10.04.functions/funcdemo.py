
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
    return num % 2 == 1



def main():
    result = add_one(9) #call
    print(result)
    result = add_one(99)
    print(result)
    result = add_one(2)
    print(result)
    result = doubler_plus_one(5)
    print(result)

main()
