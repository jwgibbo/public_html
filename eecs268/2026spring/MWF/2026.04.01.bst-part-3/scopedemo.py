def var_changer(var):
    print(var)
    var = -1 #muhahahaha
    print(var)

def main():
    num = 5
    print('main num=', num)
    var_changer(num)
    print('main num=', num)

main()
