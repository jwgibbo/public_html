def my_div(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        raise ZeroDivisionError('num2 cannot be zero')

def middle_func():
    print("welcome to middle_func!")
    ans = 0
    try:
        ans = my_div(10, 0)
    except:
        print("middle_func handling exceptions like a boss")
    print('Leaving middle_func')
    return ans

def main():
    ans = 0

    try:
        ans = middle_func()
        print(f'ans = {ans}')
    except:
        print('Something went wrong')

    print('Goodbye')
    ans = my_div(10, 0)

main()
