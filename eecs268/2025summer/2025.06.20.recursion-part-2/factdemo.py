def rec_fact(num):
    if num <= 1:
        return 1
    else:
        return num*rec_fact(num-1)

def main():
    result = rec_fact(5)
    print(result)

main()
