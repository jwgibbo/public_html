#main.py

def my_div(num1, num2):
    return num1/num2

def main():
    user_num1 = int(input('Enter a num: '))
    user_num2 = int(input('Enter a num: '))

    result = my_div(user_num1, user_num2)

    print(result)

main()
    
