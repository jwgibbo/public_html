#Goal: Define a function that takes in an int and
#      returns one more than that int
def plus_one(num):
    ans = num + 1
    return ans

def main():
    result = plus_one(5)
    print(result)
    print(plus_one(1))
    print(plus_one(3)*2)

main()
