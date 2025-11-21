def my_div(num, denom):
    if denom != 0:
        ans = num/denom
        return ans
    else:
        raise ZeroDivisionError('denom cannot be zero')

def main():
    result = 0

    print('Division about to happen...')

    try:
        print('entered try block')
        result = my_div(10, 0)
        print('result doubled =', result*2)
    except:
        print('entered except block')
        print('You broke math. Shame. SHAME.')
        print('leaving the except block')

    print('result =', result)
    print('progam ending...')

main()
