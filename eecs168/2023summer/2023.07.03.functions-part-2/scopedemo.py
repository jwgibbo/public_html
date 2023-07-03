#x = 5   #global scope, we're going
        #stop using this scope

def doubler(num):
    ans = num*2
    return ans


def main():
    num = int(input("Enter a number: "))
    print("The doubling: ", doubler(num))

main() #the program starts here
