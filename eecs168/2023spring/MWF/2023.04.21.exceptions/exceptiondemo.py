#exceptiondemo.py

def my_div(num1, num2):
    if num2 != 0:
        ans = num1 / num2
        return ans
    else:
        raise ZeroDivisionError('num2 cannot be zero')



def main():
    result = 0

    try:
        result = my_div(10, 5)
        print(result)
    except:
        print('something broke!')

    try:
        result = my_div(10, 0)
        print(result+1)
    except:
        print('something broke!')

    print('result =', result)

main()
