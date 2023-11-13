def my_div(num1, num2):
    if num2 != 0:
        return num1/num2
    else:
        raise ZeroDivisionError('num2 cannot be zero')


def main():
    result = 0

    result = my_div(10, 5)
    print(result+2)

    try:
        print('try entered')
        result = my_div(10, 0)
        print(result+2)
    except:
        print('ut oh, we broke math!')


    print('result=',result)
    print('Program ending')
    
main()
