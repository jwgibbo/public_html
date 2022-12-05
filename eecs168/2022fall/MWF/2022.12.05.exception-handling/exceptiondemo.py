def my_div(num1, num2):
    if num2 != 0:
        ans = num1 / num2
        return ans
    else:
        raise ZeroDivisionError('num2 cannot be zero!')

def no_return():
    print("You've reached the point of no return!")

def main():
    result = 0
    
    try:
        result = my_div(10, 0)
        print("Glad that went great!")
    except:
        print('Ut oh. Something broke')


    print("Result:", result)
    print('Program exiting gracefully')
    
main()
