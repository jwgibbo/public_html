#Guessing game

SECRET_WORD = 'doggy'

user_guess = input('Enter an animal: ')
user_guess = user_guess.lower()

while user_guess != SECRET_WORD:
    correct_count = 0
    #Count the number of correct letters
    #if they have the right number of letters
    if len(user_guess) == len(SECRET_WORD):
        for index in range(len(SECRET_WORD)):
            if user_guess[index] == SECRET_WORD[index]:
                correct_count = correct_count + 1
        

    user_guess = input('Enter an animal')
    user_guess.lower()
