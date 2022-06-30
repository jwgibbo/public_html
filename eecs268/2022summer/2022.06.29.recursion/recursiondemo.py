def rec_func(i):
    
    if i < 5:
        rec_func(i+1) #recursive call
        print(f'i={i}')
        
    
def main():
    print("Program started")
    rec_func(0) #initial call
    print("Program ending")

main()
