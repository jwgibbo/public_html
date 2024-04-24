import random

def heck_raiser(num):
    if num == 1:
        raise ValueError('Bad value')
    elif num == 2:
        raise RuntimeError('I hate running')
    else:
        raise ZeroDivisionError('Zero bad!')

def main():
    try:
        print('Calling heck raiser')
        heck_raiser(random.randint(1,3))
    except ValueError as error_obj:
        print(error_obj)
        print('ValueError handled')
    except RuntimeError as error_obj:
        print(error_obj)
        print('RuntimeError handled')
    except:
        print('Some other error handled')

main()
