#recursiondemo.py

def rec_func(num):
    if num <= 5:
        print(num)
        rec_func(num+1) #recursive call
        

def main():
    print('program started...')
    rec_func(1) #initial call
    print('program ending...')

main()
