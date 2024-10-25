def main():
    print('Program beginning...')
    result = 0
    print("main's result", result)
    num_changer(result)
    print("main's result", result)
    print('Program ending...')

def num_changer(result):
    print("num_changer's result", result)
    result = 99
    print("num_changer's result", result)

#call main
main()
