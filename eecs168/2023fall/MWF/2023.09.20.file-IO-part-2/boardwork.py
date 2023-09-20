file_name = input('Enter the game file name: ')
game_file = open(file_name, 'r')

game_names = []

#Extracted game names into a list
for game in game_file:
    game = game.strip()
    game_names.append(game)

print(game_names)

#Ask the user for a game name
user_game = input('Enter a game name: ')

is_found = False

#See if user_game is in the list
for game in game_names:
    if game.lower() == user_game.lower():
        #we found a match!
        is_found = True

if is_found == True:
    print('That game was on the dreamcast')
else:
    print('That game was not on the dreamcast')
    
'''
Using the keyword in

if user_game in game_names:
    print('That game was on the dreamcast')
else:
    print('That game was not on the dreamcast')
'''
