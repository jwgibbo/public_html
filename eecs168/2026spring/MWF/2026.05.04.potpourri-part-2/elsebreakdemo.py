def main():
    num = 1

    while True:
        print(num)
        num += 1
        if num > 5:
            break


    word = 'banana'
    for letter in word:
        print(letter)
        if letter == 'n':
            break
    else:
        print('did not find letter')

main()
