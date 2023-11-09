#exceptiondemo.py

def my_div(num1, num2):
    if num2 != 0:
        return num1/num2
    else:
        raise ???

def main():
    result = 0

    result = my_div(10, 0)

    print(result)

main()
