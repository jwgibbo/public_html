#fileio.py

movies_file = open('movies.txt', 'r')
poem_file = open('poem.txt', 'w')

#print all the titles
for line in movies_file:
    line = line.strip()
    if line == "Cars":
        print('That is my favorite')


#write a poem
poem_file.write('Dog food taste great!')

poem_file.close()
movies_file.close()
