def rec_print(i):
    if i <= 5:
        rec_print(i+1) #recursive call
        print(i)        
        print(f'function where i={i} is finishing')
        return



def main():
    print("Program started")
    
    rec_print(1) #initial call

    print("Program ending...")

main()
