#open our movie file
movie_file = open('movies.txt', 'r')

#read in the lines from the file
for line in movie_file:
    #print the line
    print(len(line))
