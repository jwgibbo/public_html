def my_div(num1, num2):
    if num2 != 0:
        ans = num1 / num2
        return ans
    else:
        #We shouldn't return a value
        raise ZeroDivisionError('num2 cannot be zero')

def no_return():
    print("You've reached the point of no return")
    

def main():
    result = 0 
    try:
        print('Entering try')
        result = my_div(10, 0)
    except:
        print('Something went wrong!')

    print('Result:', result+2)
    print('Anyway, how is your Thursday?')
main()
