word = 'hangehburger'
for letter in word:
    print(letter)
    if letter == 'b':
        break
print('--------------')
num = 1
while True:
    print(num)
    num += 1
    if num >= 5:
        break
print('--------------')
for i in range(10, 15):
    for j in range(1, 5):
        print(f'i={i} j={j}')
        if j == 3:
            break
print('--------------')
word = 'tacos'
target = 'z'
for letter in word:
    if letter == target:
        print('found', target)
        break
else:
    print(target, 'not found')
('--------------')
num = 1
while num < 4:
    print(num)
    num += 1
else:
    print('loop did not break')
    
