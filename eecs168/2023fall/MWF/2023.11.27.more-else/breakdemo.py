num = 1

while num < 2:
    print(num)
    num += 1
    if num >= 5:
        break
else:
    #this else is attached to the while
    #NOT the if
    print('We do not hit a break')


print('---------')

word = 'chimichanga'
target = input('Enter target: ')
for letter in word:
    if letter == target:
        print(target, 'found')
        break

else:
    #this else is attached to the loop
    #not the if
    print(target, 'not found')
