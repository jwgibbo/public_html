#fileiodemo.py

input_file = open('recipe.txt', 'r')

for line in input_file:
    line = line.strip()
    print(line)


output_file = open('favnums.txt', 'w')

for num in range(10, 101, 10):
    output_file.write(str(num)+'\n')

output_file.close()
