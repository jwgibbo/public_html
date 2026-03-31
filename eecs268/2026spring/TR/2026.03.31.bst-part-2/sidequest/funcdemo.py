def var_changer(variable):
    if variable is None:
        variable = 55

    print(variable)


def main():
    var = None
    var_changer(var)
    print(var)

main()
