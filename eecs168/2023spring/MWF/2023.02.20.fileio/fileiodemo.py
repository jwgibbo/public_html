#fileiodemo.py

#This file contain python code

#Open the file
recipe_file = open('recipe.txt', 'r')

#read in line by line
for line in recipe_file:
    line = line.strip()
    print(line)

recipe_file.close()    
