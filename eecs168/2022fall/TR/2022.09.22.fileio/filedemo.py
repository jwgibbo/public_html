#filedemo.py
recipe_file = open('recipe.txt', 'r')
copy_file = open('copy.txt', 'w')

for line in recipe_file:
    print(line, end='')
    copy_file.write(line)

recipe_file.close()
copy_file.close()
