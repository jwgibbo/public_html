#exceptiondemo.py

def my_div(num, denom):
    if denom != 0:
        ans = num/denom
        return ans
    else:
        raise ZeroDivisionError('Denominator cannot be zero')


def main():
    result = 0

    a = 10
    b = 0

    try:
        result = my_div(a, b)
        print('Division successful!')
        print('result=', result)
    except:
        print('Ut oh, you broke math.')
        print('Attempt failed')

    print('result =', result)

    print('Program ending gracefully')
    
main()
