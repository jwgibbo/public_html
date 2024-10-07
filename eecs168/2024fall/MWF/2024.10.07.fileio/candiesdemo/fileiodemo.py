#open files

candy_file = open('candies.txt', 'r')

#iterate through the file
for line in candy_file:
    line = line.strip()
    print(line)

candy_file.close()
