recipe_file = open('recipe.txt', 'r')

for line in recipe_file:
    print(line.strip())

recipe_file.close()
