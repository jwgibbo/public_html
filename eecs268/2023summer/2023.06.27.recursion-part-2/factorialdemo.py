def rec_fact(num):
    #assume num is >= 1
    if num <= 1:
        #1! ==> 1
        return 1
    else:
        return num*rec_fact(num-1)


def main():
    ans = rec_fact(3)
    print(ans)

main()
