#main.py

def my_div(num1, num2):
    if num2 != 0:
        print(num1)
        print(num2)
        return num1 / num2
    else:
        raise ZeroDivisionError('num2 cannot be zero')

def main():
    a = 10
    b = 2

    try:
        #This call is risky!
        ans = my_div(a, b)
        print('answer = ', ans)
    except:
        print('Rut roh. Something broke.')

    print('Everything went great!')

main()
