foods = {'turkey': 25, 'mac and cheese': 7, 'ham': 6}
print(foods['ham'])

foods['ham'] = 99

print(foods['ham'])

foods['yams'] = 5
print(foods['yams'])

print('ham' in foods)
print('pie' in foods)

print('-----')
for food in foods:
    print(food)

print('-----')
for food in foods.keys():
    print(food)

print('-----')
for food in foods.values():
    print(food)

print('-----')
for food, rating in foods.items():
    print(food, rating)


