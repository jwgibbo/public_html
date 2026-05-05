#breakelsedemo

def main():
    num = 1
    while True:
        print(num)
        num += 1
        if num >= 5:
            break #stop the loops

    print('-----')
    num = 1
    while num < 5:
        print(num)
        num += 1

    print('-----')
    word = 'bananarama'
    target = 'r'
    for letter in word:
        print(letter)
        if letter == target:
            break
    else:
        #code that runs if you do NOT break
        print(target, 'not found')
main()
