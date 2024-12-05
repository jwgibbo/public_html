import random

def type_error_maker():
    raise TypeError('Type Error Raised')

def value_error_maker():
    raise ValueError('Value Error Raised')


def main():
    random_num = random.randint(1, 2)

    try:
        if random_num == 1:    
            value_error_maker()
        else:
            type_error_maker()
    except TypeError as error:
        print(error)
    except ValueError as error:
        print(error)
        

main()
