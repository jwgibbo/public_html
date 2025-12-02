def my_div(num, denom):
    if denom != 0:
        result = num/denom
        return result
    else:
        raise ZeroDivisionError('denom cannot be zero')

def main():
    ans = 0

    try:
        print('try entered')
        ans = my_div(10, 0)
        print(ans*2)
        print('try finished')
    except:
        print('Oops. You broke math.')

main()
