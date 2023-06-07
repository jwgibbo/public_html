def my_div(num1, num2):
    if num2 != 0:
        ans = num1 / num2
        return ans
    else:
        raise ZeroDivisionError('num2 cannot be zero')

def middle_func(n1, n2):
    return my_div(n1, n2)

def main():
    result = -1

    try:
        result = middle_func(10, 0)
        print(result)
    except:
        print('Call to my_div failed')

    print('result =', result)
    print('Program ending...')    

main()
