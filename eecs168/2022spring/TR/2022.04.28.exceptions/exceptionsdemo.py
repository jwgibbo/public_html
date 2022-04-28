#exceptionsdemo.py

def my_div(num1, num2):
    if num2 != 0:
        return num1/num2
    else:
        raise ZeroDivisionError('num2 cannot be zero')

def main():

    is_age_valid = False
    
    while not is_age_valid:
        try:
            user_age = int(input('Enter your age: '))
            is_age_valid = True
            print('You are ', user_age, ' years old')
        except:
            print('Please enter a valid age')
        
    print('Program ending...')
    
main()
