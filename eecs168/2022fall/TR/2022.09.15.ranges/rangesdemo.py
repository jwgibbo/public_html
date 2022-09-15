#Goal print value 1 to 5

num = 1
while num < 6:
    print(num)
    num += 1

print('=======')

for num in range(1, 6):
    print(num)
    
print('=======')

word = 'pineapple'
for letter in word[2:5]:
    print(letter)

print('=======')

for outer_num in range(2, 6):
    for inner_num in range(1, 4):
        print("outer_num =", outer_num, "inner_num =", inner_num)

print('=======')

for row in range(4):
    for col in range(5):
        print(col+1, end='')
    print('')
    
