#Define a recursive factorial
def rec_fact(n):
    if n <= 1:
        return 1
    else:
        return n*rec_fact(n-1)

def main():

    ans = rec_fact(1)
    print(ans)
    ans = rec_fact(2)
    print(ans)
    ans = rec_fact(5)
    print(ans)


main()
