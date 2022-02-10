
#Goal: Store 5 numbers

num1 = 10
num2 = 20
num3 = 30
num4 = 40
num5 = 50


nums = []
#Append 10,20,30,40,50 to nums
#with a while loop
value = 10
while value <= 1000:
    nums.append(value)
    value = value + 10

#print only multiple of 50 that
#are in my list
for num in nums:
    if num % 50 == 0:
        print(num)
