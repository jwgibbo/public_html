#define a function that takes an int and
#returns one more than that int
def plus_one(num):
    ans = num + 1
    #FREEZE and look at the call stack
    return ans

def main():
    user_num = int(input('enter num: '))
    result = plus_one(user_num) #function call
    print(result)
    result = plus_one(99)
    print(result)

main()
