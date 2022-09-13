fruit = 'orange'

#Using while loop then a for-in loop
#print the string backwards

index = -1
while index>= -len(fruit):
    print(fruit[index])
    index = index - 1

print('==========')

reversed_fruit = fruit[::-1]
for letter in reversed_fruit:
    print(letter)

#Goal: print all E's
word = 'Every'

for letter in word:
    if letter == 'E' or letter == 'e':
        print(letter)
