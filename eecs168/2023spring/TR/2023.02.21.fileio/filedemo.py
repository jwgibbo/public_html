#filedemo.py

#Goal: open 'recipe.txt' and print its
#       contents to the user

recipe_file = open('recipe.txt', 'r')

for line in recipe_file:
    line = line.strip()
    print(line)

recipe_file.close()
