
def rec_func():
    i = 0
    if i < 4:
        print('i=',i)
        rec_func() #recursive call

    i += 1


def main():
    rec_func() #initial call

main()

    
