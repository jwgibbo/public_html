#function defintion
def add_one(num):
    answer = num + 1
    return answer


def main():
    answer = 5
    result = add_one(99)
    print(result)
    print(answer)

#only "global" call
main()
