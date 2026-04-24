#exceptions.py

def my_div(a, b):
    if b != 0:
        return a/b
    else:
        raise ZeroDivisionError('b cannot be zero')

def main():
    result = my_div(10, 0)
    print(result)
    print('result doubled =', result*2)

main()
