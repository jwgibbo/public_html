nums = [5, 55, 10, 7, 55, 42, 9, 55]

#Ask the user for a number and tell them if
#it is in the list

user_num = int(input('Enter a number: '))

#Solve this WITHOUT using keyword in
is_val_in_list = False
for num in nums:
    if num == user_num:
        #It's in the list!
        is_val_in_list = True


if is_val_in_list:
    print('Your number is in the list')
else:
    print('Your number is NOT in the list')

#Now solve it with keyword in
if user_num in nums:
    print('Your number is in the list')
else:
    print('Your number is NOT in the list')
