def my_div(num1, num2):
    if num2 != 0:
        ans = num1/num2
        return ans
    else:
        raise ZeroDivisionError('num2 cannot be zero')

def main():
    ans = 55

    try:
        ans = my_div(10, 0)
        print('In the try: ', ans)
    except:
        print('Ut oh! It broke!')

    print('After the try-except: ', ans)


main()
