def func(num, word):
    print(f'num = {num}')
    print(f'word = {word}')


def main():
    func(5, 'panda')
    print('======')
    func('panda', 5)
    print('======')
    func(num=5, word='panda')
    print('======')
    func(word='panda', num=5)


main()
