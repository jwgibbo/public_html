word = 'serendipity'
for letter in word:
    print(letter)
    if letter == 'z':
        break
else:
    print('letter not found')

print('----------')

#Use sparingly
num = 1
while num >= 3:
    if num >= 5:
        break
    print(num)
    num += 1
else:
    print('while did not hit a break')
