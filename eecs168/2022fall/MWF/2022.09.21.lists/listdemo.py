

nums = [] #Create an empty list

#Get five values from the user
for num in range(5):
    user_num = int(input('Enter a number: '))
    nums.append(user_num)


#print values in the list
for num in nums:
    print(num)

#You can print a list all at once
print(nums)
