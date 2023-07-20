#exceptiondemo.py

def my_div(num1, num2):
    if num2 != 0:
        ans = num1 / num2
        return ans
    else:
        raise ZeroDivisionError('num2 cannot be zero')

def main():
    result = -99
    print(result)

    try:
        result = my_div(10, 0)
        print(result+2)
    except ArithmeticError as math_error:
        print('Math Error occured')
        print(math_error)
    except ZeroDivisionError as my_error:
        print('Math broke!')
        print(my_error)

    print(f'result={result}')
    print('Program ending...')

main()
