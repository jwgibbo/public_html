#Goal: Obtain 50 ints from the user

nums = []

for num in range(5):
    user_value = int(input("Enter a number: "))
    nums.append(user_value)

nums[0] = 9001

for num in nums:
    print(num)
