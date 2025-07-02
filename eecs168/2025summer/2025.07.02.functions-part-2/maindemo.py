#Goal: Define a function that takes in a number
#       and returns one more than that number

def plus_one(num):
    answer = num + 1
    return answer

def greeter(name):
    print('Welcome,', name)
    print('We are going to do some math today...')
    return

def main():
    user_name = input('Enter your name: ')
    greeter(user_name)
    test = greeter('Q-Bert') #Don't try this at home
    print(test)
    print(type(test))
    

main() #only global level call
