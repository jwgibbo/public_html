word = 'wombat'
for letter in word:
    if letter == 'z':
        break
    else:
        print(letter)
else:
    print('loop was not broken out of')
