#filedemo.py

movies_file = open('movies.txt', 'r')

for title in movies_file:
    title = title.strip()
    print(title)

movies_file.close()
