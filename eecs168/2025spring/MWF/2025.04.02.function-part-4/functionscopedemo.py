def num_changer(num):
    print("num_changer's num =", num)
    num = 99
    print("num_changer's num =", num)

def main():
    my_num = 5
    num_changer(my_num)
    print("main's my_num =",my_num)

main() #only thing we do at the global scope
