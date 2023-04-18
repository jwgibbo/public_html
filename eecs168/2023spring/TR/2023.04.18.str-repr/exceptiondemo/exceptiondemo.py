#exceptiondemo.py


def my_div(num1, num2):
    if num2 != 0:
        ans = num1 / num2
        return ans
    else:
        #raise an exceptions

def main():
    result = 0

    result = my_div(10, 5)
    print(result)
    
    result = my_div(10, 0)
    print(result + 1)

main()
