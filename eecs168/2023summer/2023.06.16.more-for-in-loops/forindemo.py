word = 'friday'

for letter in word:
    print(letter)

print('------------')

#You can create/choose your iterable in
#the for in loop
for letter in 'lifeforce':
    print(letter)

print('------------')

for num in range(1, 6):
     print(num)

print('------------')

for num in range(10, 0, -1):
    print(num)

print('------------')

#Goal: Use a for in loop to
#       increase a variable's value
#       by 1 five times
target = 10
for num in range(1, 6):
    target = target + 1
    print(target)
