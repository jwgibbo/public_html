#define a recursive factorial
def rec_fact(n):
    if n <= 1:
        return 1
    else:
        return n*rec_fact(n-1)

def main():
    print(rec_fact(4))

main()
