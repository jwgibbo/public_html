
def plus_one(num):
    ans = num + 1
    print("num's id: ", id(num))
    print("ans's id: ", id(ans))
    return ans

def main():
    x = 5
    print("x's id: ", id(x))
    y = plus_one(x)
    print("y's id: ", id(y)) 
    print(y)


main()
