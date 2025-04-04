def main():
    candies = {}
    candies['peeps'] = 2
    candies['cadberry eggs'] = 10
    candies['jelly beans'] = 5.5
    candies['gummies'] = 10
    candies['cadberry eggs'] = 9.9
    
    print(candies)
    print(len(candies))

    for candy in candies:
        print(candy, '=', candies[candy])

    for candy, rating in candies.items():
        print(candy, '=', rating)


main()
