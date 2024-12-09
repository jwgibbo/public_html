import random

def raise_random_error():
    choice = random.randint(1, 3)
    if choice == 1:
        raise ValueError('random value error')
    elif choice == 2:
        raise TypeError('random type error')
    else:
        raise ZeroDivisionError('random zero-div error')

def main():

    try:
        raise_random_error()
    except ValueError as error:
        print(error)
    except TypeError as error:
        print(error)
    except ZeroDivisionError as error:
        print(error)
main()
    
