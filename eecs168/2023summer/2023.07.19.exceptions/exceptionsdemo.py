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
    except ZeroDivisionError:
        print('Math broke!')

    print(f'result={result}')
    print('Program ending...')

main()
