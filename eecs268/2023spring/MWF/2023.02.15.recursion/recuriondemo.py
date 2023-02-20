def rec_print(i):
    if i < 5:
        print(i)
        rec_print(i+1) #recursive call
        return


def main():
    print('Program started')

    rec_print(0) #initial call

    print('Program ending...')



main()
