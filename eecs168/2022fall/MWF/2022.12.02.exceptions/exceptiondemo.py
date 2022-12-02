def my_div(num1, num2):
    if num2 != 0:
        ans = num1 / num2
        return ans

def no_return():
    print("You've reached the point of no return!")

def main():
    result = 0

    result = my_div(10, 0)

    print(result+2)
    
main()
