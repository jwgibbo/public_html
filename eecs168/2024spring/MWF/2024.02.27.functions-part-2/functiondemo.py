#Goal: Define a function that takes a number
#       and returns one more than that number
def add_one(num):
    ans = num + 1
    #FREEZE and look at the call stack
    return ans

def main():
    result = add_one(4) 
    print(result)

main() 
