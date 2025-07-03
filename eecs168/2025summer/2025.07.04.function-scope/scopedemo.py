
def num_changer(num):
    print("num_changer's num =", num)
    num = 99
    print("num_changer's num =", num)
    return

def main():
    num = 5
    print("main's num =", num)
    num_changer(num) #Assigns num_changer's num to 5
    print("main's num =", num)

main()#first call on the call stack

    
