def bad_recipe():
    #cause ValueError
    result = float('rootbeer')
    return result

def main():
    result = 0
    
    try:
        result = 10/0
    except (TypeError, ValueError):
        print('Ut oh TypeError or ValueError raised!')
    except Exception as err:
        print(err)
        print('Handle some kind of error')


main()

