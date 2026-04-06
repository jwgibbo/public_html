#dictdemo.py

def main():
    space_movies = {}
    space_movies['Interstellar'] = 2014
    space_movies['Spaceballs'] = 1987
    space_movies['Project Hail Mary'] = 2026
    space_movies['Space Jam'] = 1996
    space_movies['Wall-E'] = 2008
    space_movies['Jason X'] = 2001

    print(space_movies)
    print(type(space_movies))
    print(len(space_movies))

    print('----------')

    for title in space_movies.keys():
        print(title)

    print('----------')

    for year in space_movies.values():
        print(year)

    print('----------')

    for title, year in space_movies.items():
        print(title, 'was made in', year)
    
main()
