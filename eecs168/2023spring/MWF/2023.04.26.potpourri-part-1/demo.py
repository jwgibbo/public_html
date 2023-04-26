def main():
    words = ['zoom', 'call', 'I', 'no', 'like']
    for word in words:
        print(word)
        if word == 'me':
            break
            #stop the loop
    else:
        print('Did not find me')

    user_num = 0

    while user_num != 55:
        user_num = int(input('Guess the number: '))
    else:
        print('while else running...')
        
         
main()
