def my_div(num1, num2):
    if num2 != 0:
        ans = num1/num2
        return ans
    else:
        raise ZeroDivisionError('num2 cannot be zero')


def main():
    try:
        result = my_div(10, 2)
        print(result+2)
    except:
        print('Sorry, you broke math')

main()
