word = 'back pain!'

for letter in word:
    if letter == 'z':
        break
    else:
        print(letter)
else:
    print('no z found')
