#fileidemo.py

recipe_file = open('recipe.txt', 'r')

for line in recipe_file:
    line = line.strip()
    print(line)
