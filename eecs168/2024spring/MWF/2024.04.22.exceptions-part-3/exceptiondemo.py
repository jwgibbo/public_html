import random

def fun_raiser(num):
    if num == 1:
        raise IndexError('bad index')
    elif num == 2:
        raise ValueError('bad value')
    else:
        raise ZeroDivisionError('bad zero')

def main():

    random_choice = random.randint(1, 3)
    print(f'Current choice = {random_choice}')
    try:
        fun_raiser(random_choice)
    except ValueError as error:
        print('The value was wrong')
        print(error)
    except IndexError as error:
        print('Invalid index')
        print(error)
    except ZeroDivisionError as error:
        print('something went wrong')
        print(error)
    
main()
