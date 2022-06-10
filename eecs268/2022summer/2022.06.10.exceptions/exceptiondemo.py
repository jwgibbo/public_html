
def my_div(num1, num2):
    if num2 != 0:
        ans = num1/num2
        return ans
    else:
        #We need an alternative to
        #returning a value
        raise ZeroDivisionError('num2 cannot be zero')
    


def main():
    ans = 0

    try:
        print("We're in the try now!")
        ans = my_div(10, 0)
        print("ans =", ans)
    except:
        print('Ut oh! Something broke!')

    

main()
