def rec_print(i):
    if i <= 5:
        rec_print(i+1) #recursive call
        print(i)
        return



def main():
    print("Program started")
    
    rec_print(1) #initial call

    print("Program ending...")

main()
