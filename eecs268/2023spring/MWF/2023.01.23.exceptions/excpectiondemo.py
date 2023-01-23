def my_div(num1, num2):
    if num2 != 0:
        ans = num1 / num2
        return ans
    else:
        raise ZeroDivisionError("num2 cannot be zero")


def main():
    result = 99

    print("Program started")

    try:
        result = my_div(10, 0)
        print(result+2)
    except:
        print("Ut oh! Something broke!")

    print("result:", result)

    print("Program ending")
main()
