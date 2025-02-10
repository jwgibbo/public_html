text = 'abc'
for character in text:
    print(character)

print('----------')

for number in range(5):
    print(number)

print('----------')

for number in range(15, 20):
    print(number)

print('----------')

for number in range(1, 10, 3):
    print(number)

print('----------')

start = int(input('Enter a start: '))
stop = int(input('Enter a stop: '))
step = int(input('Enter a step: '))
for num in range(start, stop, step):
    print(num)

print('----------')

#Goal: Sum up and print the value from 1 to 5
total = 0
for num in range(1, 101):
    total = total + num
    print('num =', num, 'total =', total)

