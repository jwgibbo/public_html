user_word = input('Enter a word: ')
count = 0
for letter in user_word:
    if letter == 'an':
        count = count + 1
    print(letter)

print('Count of an\'s: ', count)

print('==========')
#Solving the board word with slices

user_word = input('Enter a word: ')
wow_count = 0
for index in range(0, len(user_word)):
    if user_word[index:index+3] == 'wow':
        wow_count = wow_count + 1

    print(f'{user_word[index:index+3]} count = {wow_count}')

print('========')
#Solve board work with index lookups
user_word = input('Enter a word: ')
wow_count = 0
for index in range(0, len(user_word)-2):
    if user_word[index] == 'w' and user_word[index+1] == 'o' and user_word[index+2] == 'w':
        wow_count = wow_count + 1

    print(f'{user_word[index:index+3]} count = {wow_count}')
