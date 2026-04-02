def main():
    space_movies = {}
    print(space_movies)
    print(type(space_movies))
    space_movies['Star Wars'] = 1977
    space_movies['The Martian'] = 2015
    space_movies['Project Hail Mary'] = 2026
    space_movies['Jason X'] = 2001
    space_movies['Spaceballs'] = 1987
    space_movies['Alien'] = 1979

    print(space_movies)
    print('length = ', len(space_movies))
    print(space_movies['Alien'])

    print('-------------')

    for title in space_movies.keys():
        print(title)

    print('-------------')

    for year in space_movies.values():
        print(year)

    print('-------------')

    for title, year in space_movies.items():
        print(title, 'was made in', year)

    print('Alien' in space_movies)
main()
