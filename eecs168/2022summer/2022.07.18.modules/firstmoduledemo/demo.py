#import the code from mymodule.py
import mymodule

def main():
    user_choice = ''

    while not mymodule.is_any_y(user_choice):
        user_num = mymodule.positive_user_num()
        print(f'Sum of 1 to {user_num} = {mymodule.num_sum(user_num)}')
        user_choice = input("Do you want to exit?: ")

main()
