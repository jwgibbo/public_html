movies = {}

movies['Halloween'] = 6
movies['Hocus Pocus'] = 3
movies['Monster House'] = 5
movies['Shining'] = 9
movies['Conjuring'] = 7

for title in movies.keys():
    print(f'{title} has a spooky rating of', movies[title])

for spooky_num in movies.values():
    print(spooky_num)

for title, spooky_num in movies.items():
    print(f'{title} has spooky rating of {spooky_num}')

print('Halloween' in movies)
