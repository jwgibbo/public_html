#open files

candy_file = open('candies.txt', 'r')

#iterate through the file
for line in candy_file:
    print(line)
