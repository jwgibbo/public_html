def my_div(num1, num2):
    if num2 != 0:
        return num1/num2
    else:
        raise ZeroDivisionError('num2 cannot be zero')
        print('being in the function rules!')

def main():
    user_num1 = int(input('Numerator: '))
    user_num2 = int(input('Denominator: '))

    result = 0 #create and initialize result
    try:
        result = my_div(user_num1, user_num2)
        print(f'result+2 = {result+2}')
    except:
        print('Ut oh, you broke math')


main()
