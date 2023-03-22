def one_more(num):
    ans = num + 1
    num = -99
    return ans

def say_hi():
    print('Hi!')
    return

def main():
    say_hi()
    num = int(input('Enter a number: '))
    result = one_more(num)
    print('Did you know that one more than', num, 'is', result,'?')


#The one "top level" call
main()
