word = 'birthday'

index = 0

while index < len(word):
    print(word[index])
    index = index + 1

print("After the loop, index = " + str(index))


print('===========')
#This is the more "pythonic" solution
for letter in word:
    print(letter)

print("After the loop, letter = " + letter)
