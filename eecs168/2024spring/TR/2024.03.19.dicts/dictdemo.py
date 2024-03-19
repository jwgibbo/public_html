movies = {}
movies['trolls'] = 7
movies['dune2'] = 8
movies['oppenheimer'] = 10
movies['puss in boots'] = 7
movies['barbie'] = 9

print(movies)
movies.pop('trolls')
print(movies)

for movie in movies.keys():
    print(movie)

for rating in movies.values():
    print(rating)

for movie, rating in movies.items():
    print(f'{movie} has a rating of {rating}')
