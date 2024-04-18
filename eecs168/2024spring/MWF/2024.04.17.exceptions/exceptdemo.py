#main.py

def my_div(num1, num2):
    if num2 != 0:
        return num1/num2
    else:
        raise ZeroDivisionError('num2 cannot be zero')

def main():
    user_num1 = int(input('Enter a num: '))
    user_num2 = int(input('Enter a num: '))

    try:
        result = my_div(user_num1, user_num2)
        print(result+2)
    except:
        print('Ut oh. Math broke!')

main()
    
