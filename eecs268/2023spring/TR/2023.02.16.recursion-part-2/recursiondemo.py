#Goal: define a recursive factorial function
def rec_factorial(num):
    if num <= 1:
        return 1
    else:
        return num*rec_factorial(num-1)


def main():
    ans = rec_factorial(1)
    print(ans)
    ans = rec_factorial(2)
    print(ans)
    ans = rec_factorial(3)
    print(ans)

main()
