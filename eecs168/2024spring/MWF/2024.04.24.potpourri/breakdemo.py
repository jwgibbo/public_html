word = 'potpourri'
target = 'z'
for letter in word:
    print(letter)
    if letter == target:
        break
else:
    #code only runs if the break was not hit
    print('target not found')
    
print('--------------')

num = 1
while num <= 10:
    print(num)
    num += 1

print('--------------')

for i in range(10, 14):
    for j in range(20, 24):
        print(f'i={i} j={j}')
        if j == 22:
            break

print('--------------')
