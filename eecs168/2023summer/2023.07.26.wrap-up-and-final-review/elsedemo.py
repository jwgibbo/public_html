def for_in_demo():
    nums = [5, 10, 15, 20, 25, 30, 35]
    for num in nums:
        if num % 5 == 0 and num % 7 == 0:
            print(num)
            break
    else:
        print('Did not find a match')

def while_demo():
    num = 1
    while num < 10:
        if num % 7 == 0:
            break
        print(num)
        num += 5
    else:
        print('Break not hit')

def main():
    while_demo()
main()
