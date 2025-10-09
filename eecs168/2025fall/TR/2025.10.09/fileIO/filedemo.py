#filedemo.py

candy_file = open('candies.txt', 'r')

for line in candy_file:
    line = line.strip()
    print(line)

candy_file.close()


output_file = open('dad.txt', 'w')
output_file.write('Luna! Luna!\n')
output_file.write('Look over here!')
output_file.close()

