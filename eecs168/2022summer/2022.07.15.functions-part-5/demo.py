def is_any_y(sequence):
    if sequence == 'y' or sequence == 'Y':
        return True
    else:
        return False

def is_positive(num):
    if num > 0:
        return True
    else:
        return False

def positive_user_num():
    user_num = 0
    while not is_positive(user_num):
        user_num = int(input('Enter a positive value: '))

    return user_num

def num_sum(upper_bound):
    total = 0
    for num in range(upper_bound+1):
        total = total + num
    return total

def main():
    user_choice = ''

    while not is_any_y(user_choice):
        user_num = positive_user_num()
        print(f'Sum of 1 to {user_num} = {num_sum(user_num)}')
        user_choice = input("Do you want to exit?: ")

main()
