x = 99 #globally declared

def global_nonsense():
    print(x)
    x += 1
    print(x)

def add_one(num):
    ans = num + 1
    return ans

def evil_func(num):
    num = -1
    print("num is now", num)
    print("Muhahahaha!")
    return num

def main():
    num = 55
    print(num)
    evil_func(num)
    print(num)
    print("starting global nonsense")
    #global_nonsense() #will cause crash

#The one and only thing we do at
#the global scope is call main

main() #call to main
