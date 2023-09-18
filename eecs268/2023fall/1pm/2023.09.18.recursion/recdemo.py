def rec_func():
    print('Hello')
    rec_func() #recursive call

def main():
    print('Program started')
    rec_func() #initial call
    print('Program ending')

main()
