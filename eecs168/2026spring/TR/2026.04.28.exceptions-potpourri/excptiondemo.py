#exceptiondemo.py

def trouble_maker(choice):
    if choice == 1:
        raise RuntimeError('runtime issue')
    elif choice == 2:
        raise ZeroDivisionError('math broke')
    else:
        raise KeyError('Cannot find my keys')

def main():
    try:
        trouble_maker(3)
    except RuntimeError:
        print('Runtime Error handled')
    except ZeroDivisionError:
        print('Zero division? No prob!')
    except:
        print('catch all handler')

    print('Program exiting...')

main()
