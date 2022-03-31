def func(num, word):
    print(num)
    print(word)


def main():
    func(5, 'cat')
    print('-----')
    func('cat', 5) #position changed
    print('-----')
    func(num=5, word='cat')
    print('-----')
    func(word='cat', num=5)
    
    
main()
