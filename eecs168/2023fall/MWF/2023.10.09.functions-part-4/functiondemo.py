def print_menu():
    #the menus is printed

def is_peas(letter):
    #check if letter is a p or P

def is_apples(letter):
    #check if letter is a or A


def main():
    print_menu()

    user_choice = input('Which food do you want?: ')

    if is_peas(user_choice):
        print('That will be $2.00')
    elif is_apples(user_choice):
        print('That will be $1.00')
    else:
        print('Sorry we don\'t sell what you want')

    print('Goodbye')
main()
