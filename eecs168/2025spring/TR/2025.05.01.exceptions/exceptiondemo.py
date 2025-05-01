def my_div(num1, num2):
    if num2 != 0:
        ans = num1/num2
        return ans
    else:
        raise ZeroDivisionError('num2 cannot be zero')


def main():
    result = 0

    try:
        print('try entered...')
        result = my_div(10, 0)
        print(result+1)
        print('try ending...')
    except:
        print('Ut oh. Math broke.')

    print('Program ending...')
main()
