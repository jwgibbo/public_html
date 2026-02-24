#factorial.py

def rec_factorial(num):
    if num == 1:
        return 1
    else:
        return num*rec_factorial(num-1)


def main():
    ans = rec_factorial(2)
    print(ans)

main()
