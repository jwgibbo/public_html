#divisiondemo.py

def my_div(num1, num2):
    if num2 != 0:
        ans = num1 / num2
        return ans

def main():
    result = 0

    result = my_div(10, 0)
    print(result+2)

main()
