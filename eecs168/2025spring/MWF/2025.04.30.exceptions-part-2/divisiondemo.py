#divisiondemo.py

def my_div(num1, num2):
    if num2 != 0:
        ans = num1 / num2
        return ans
    else:
        raise ZeroDivisionError('num2 cannot be zero!')

def main():
    result = 0

    try:
        print('try entered')
        result = my_div(10, 5)
        print(result+2)
        print('try is over')
    except:
        print('Math broke. Sorry.')

    print('result =', result)
    print('Program ending...')

main()
