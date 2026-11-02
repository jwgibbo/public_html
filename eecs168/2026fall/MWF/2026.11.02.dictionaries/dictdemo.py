food_ratings = {}

food_ratings['turkey'] = 6
food_ratings['stuffing'] = 10
food_ratings['taters'] = 6
food_ratings['pies'] = 7


print(food_ratings['stuffing'])

#Iterate over keys
for food in food_ratings:
    print(food)

print('---------')


for food in food_ratings.keys():
    print(food)

print('---------')

for rating in food_ratings.values():
    print(rating)

print('---------')

for food, rating in food_ratings.items():
    print(food, 'rating:', rating)
