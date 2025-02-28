#editdemo.py

nums = [5, -10, -15, 20]
print(nums)
#Goal: Change all negative values to their
#       absolute values
for num in nums:
    print(num)
    num = 0
    print(num)

print(nums)


for index in range(0, len(nums)):
    nums[index] = 0

print(nums)
