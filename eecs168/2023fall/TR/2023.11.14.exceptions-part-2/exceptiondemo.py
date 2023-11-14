#exceptiondemo.py

def my_div(num1, num2):
    if num2 != 0:
        return num1/num2
    else:
        raise ZeroDivisionError('num2 cannot be zero')
    


def main():
    result = 0

    try:
        result = my_div(10, 0)
    except:
        print('Ut oh, math broke')

    print(result)
    print('program ending...')

main()
