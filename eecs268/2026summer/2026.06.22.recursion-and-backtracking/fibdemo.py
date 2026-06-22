#fibdemo.py

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num-1) + fib(num-2)

def main():
    print('Program beginning...')
    result = fib(8)
    print('result', result)
    print('Program ending...')

main()
