
#Variables I will use
user_choice = '' #empty string
user_amount = 0
total = 0

#Constants (values that won't change)
#In python, a convention (aka a good
#practice) is to name constant all-caps
PASTA_PRICE = 15.00
TACO_PRICE = 0.75

#Ask the user for their choice
#Obtain either a p/P or a t/T
user_choice = input("Do you want pasta (p/P) or tacos (t/T): ")

#Ask them how many they want
user_amount = int(input("How many do you want?: "))

#Figure out which they chose
if user_choice == 'p' or user_choice == 'P':
    total = user_amount * PASTA_PRICE

if user_choice == 't' or user_choice == 'T':
    total = user_amount * TACO_PRICE

#Calculate and print a total
print(f'Your total is ${total}')
