#Goal: Define a function that takes a
#       number and returns one more than
#       that number
def add_one(num):
    ans = num + 1
    return ans

def main():
    #We need to call our function
    user_num = int(input('Enter num: '))
    result = add_one(user_num)
    print(result)
    print(add_one(99))

#Only line at the global scope
main() #entry point to the program
