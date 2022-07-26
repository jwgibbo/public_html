#main.py


def my_div(num1, num2):
    if num2 != 0:
        ans = num1/num2
        return ans
    else:
        raise ZeroDivisionError('num2 cannot be zero')

    print("That's the end of my_div...")

def main():

    print('Program beginning')

    result = 0
    
    try:
        result = my_div(10, 0)
        print(f'result={result}')
        print('hey what about this print?')
    except:
        print('Ut oh, something bad happened')
        
    print(result)
    print('Program ending')

main()
