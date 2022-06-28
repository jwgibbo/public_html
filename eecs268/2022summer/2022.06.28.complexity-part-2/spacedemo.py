#Algorthim 1

base = float(input("Enter a base: "))
height = float(input("Enter a height: "))
area = 1/2*base*height

#Quick side note python doesn't cap ints

#Algorithm 2
user_size = int(input("How many numbers do you need to store?: "))
user_nums = []

for i in range(user_size):
    temp = float(input("Enter a number: "))
    user_nums.append(temp)
    
