def main():
    candies = {}
    candies['peeps'] = 2.5
    candies['jelly beans'] = 5
    candies['cadburry egg'] = 10
    candies['rice crispy treats'] = 7
    candies['chocolate bunny'] = 7

    print(candies)
    print(candies['peeps'])
    print(len(candies))
    print('-----------')
    for candy in candies:
        print(candy)

    print('-----------')
    for candy in candies.keys():
        print(candy)

    print('-----------')
    for rating in candies.values():
        print(rating)

    print('-----------')
    for candy, rating in candies.items():
        print(candy, '=', rating)
    

    

main()
