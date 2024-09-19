#Goal: Calculate the sum of 1 to 50

total = 0

print('num\ttotal')
for num in range(1, 51):
    total = total + num
    print(f'{num}\t{total}')

print('======')
print(total)
