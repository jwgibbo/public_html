def my_div(num1, num2):
    print('Entering my_div')

    if num2 != 0:
        return num1/num2
    else:
        raise ZeroDivisionError("num2 cannot be zero")
    
    print('Leaving my_div')
    
    

def main():
    ans = my_div(10, 5)
    print(ans)
    
    try:
        ans = my_div(10, 0)
        print(ans)
    except:
        print('Ut oh! Something broke.')

    print(f"ans = {ans}")
    
if __name__ == '__main__':
    main()
