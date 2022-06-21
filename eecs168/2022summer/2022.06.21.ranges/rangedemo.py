

#print all even numbers from 2 to 22
for num in range(2, 23, 2):
    print(num)

print('=====')

#print all odd numbers from 17 down to 1
for num in range(17, 0, -2):
    print(num)

print('=====')

#Calculate the sum of value from 1 to 5
my_sum = 0
for num in range(1, 6):
    my_sum = my_sum + num
    print(f'num = {num}\tmy_sum = {my_sum}')
    
#Print 'Hooooot!' with user chosen o's
num_os = int(input('How many O\'s?: '))
all_the_os = ''

for num in range(num_os):
    all_the_os = all_the_os + 'o'

print("H" + all_the_os + "t!")
