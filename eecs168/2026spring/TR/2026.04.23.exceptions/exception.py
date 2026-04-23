#exception.py

def my_div(a, b):
    if b != 0:
        return a/b
    else:
        raise ZeroDivisionError('b cannot be zero')

def main():
    result = 0
    try:
        print('Try entered')
        result = my_div(10, 0)
        print('result =', result)
        print('Try over')
    except:
        print('Oops, math broke.')

    
    print('Program exiting with grace.')
main()
