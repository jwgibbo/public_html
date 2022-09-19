#print the values 1 to 5

for num in range(1, 6, 1):
    print(num)

print('=====')

#print the values 0 to 9

for num in range(10):
    print(num)

print('====')

#print even values from 2 to 22

for num in range(2, 23, 2):
    print(num)

#make a string with 1000 a's
scream = ''
for num in range(1000):
    scream = scream + 'a'

scream = scream + 'h!'
print(scream)

print('=====')

for outer_num in range(1, 4):
     for inner_num in range(2, 8):
           print('outer_num=', outer_num,'inner_num=', inner_num)
