candies = {}

candies['snickers'] = 10
candies['black_licorice'] = 2
candies['candy corn'] = 5
candies["reese's"] = 10

print(candies)
print(candies['snickers'])

for candy in candies:
    print(candy)

for rating in candies.values():
    print(rating)

for candy, rating in candies.items():
    print(f'{candy} has a rating of {rating}')
