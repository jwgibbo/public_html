#exceptions.py

def my_div(a, b):
    if b != 0:
        return a/b
    else:
        raise ZeroDivisionError('b cannot be zero')

def main():
    print('Program staring...')
    result = 0
    try:
        print('entered try')
        result = my_div(10, 5)
        print(result)
        print('result doubled =', result*2)
        print('try finished')
    except:
        print('except block entered')
        print('Whoops, math broke')
        
    print('result final value =', result)
    print('Program ending...')

main()
