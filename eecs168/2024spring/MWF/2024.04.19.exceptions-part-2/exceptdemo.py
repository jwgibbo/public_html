#main.py

def my_div(num1, num2):
    if num2 != 0:
        return num1/num2
    else:
        raise ZeroDivisionError('num2 cannot be zero')

def middle_func(num1, num2):
    print('Entering middle_func')
    result = my_div(num1, num2)
    print('Leaving middle func')
    return result

def main():
    user_num1 = int(input('Enter a num: '))
    user_num2 = int(input('Enter a num: '))

    result = 0

    try:
        result = middle_func(user_num1, user_num2)
        print(result+2)
    except:
        print('Ut oh. Math broke!')

    print('result after trying', result)
main()
    
