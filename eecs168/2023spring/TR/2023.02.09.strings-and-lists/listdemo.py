#Goal: Obtain 5 numbers from the user

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
num4 = int(input("Enter a number: "))
num5 = int(input("Enter a number: "))

print(num1, num2, num3, num4, num5)

print('=======')

user_nums = [] #empty list

#Ask the user for a number five times
count_obtained = 0
while count_obtained < 5:
    #get a number from the user
    temp_num = int(input('Enter a number: '))
    
    #append it to the list
    user_nums.append(temp_num)

    #increment count
    count_obtained = count_obtained + 1

print(user_nums)
