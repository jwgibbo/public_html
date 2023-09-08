#Goal print the values 1 to 5
for num in range(1, 6):
    print(num)

print('===========')

#print all the multiples of 7 from 7 to 49
for num in range(7, 50, 7):
    print(num)

print('===========')

#calculate the sum of value from 1 to 5
total = 0
for num in range(1, 6):
    total = total + num
    print('num =', num, '\ttotal =', total)
