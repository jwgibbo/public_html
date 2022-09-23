def rec_func(i):
    if i < 3:
        rec_func(i+1) #recursive call
        print(i)

def rec_fact(num):
    if num <= 1:
        return 1
    else:
        return num*rec_fact(n-1)
    

def main():
    
    print(rec_fact(5))
        


main()
