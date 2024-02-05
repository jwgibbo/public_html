word = 'pizza'
for character in word:
    print(character)

print('=============')

for num in range(2, 10, 3):
    print(num)

print('=============')

#Goal: add the values 1 to 5
total = 0
print('num \t total')
print('-----------')
for num in range(1, 6):
    total = total + num
    print(num,'\t',total)
