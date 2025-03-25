recipe_file = open('catfood.txt', 'r')

for line in recipe_file:
    print(len(line.strip()))

recipe_file.close()
