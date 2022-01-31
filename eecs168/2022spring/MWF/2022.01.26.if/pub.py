#Goal: Ask the user for their age.
#      If they are 21 or over, say "Welcome
#       to the pub!" otherwise you say "Scram"


user_age = int(input("Enter your age ?"))
if user_age >= 21:
    print("Welcome to the pub!")
else:
    print("Scram!")
