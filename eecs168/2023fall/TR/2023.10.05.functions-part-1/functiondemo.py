#Write a function that takes a number
#and returns one more than that number

def plus_one(num):
    ans = num + 1
    return ans

def repeat_print(misdeed, count):
    for num in range(count):
        print('I will not', misdeed)
    
def main():
    result = plus_one(5) #function call
    print(result)
    print(plus_one(99))
    print(plus_one(4)*plus_one(2))
    repeat_print('cheat', 5)

main()
