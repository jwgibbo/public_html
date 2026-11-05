food_dict = {}

food_dict['turkey'] = 1
food_dict['stuffing'] = 3
food_dict['pies'] = 8
food_dict['mac&cheese'] = 8

food_dict['turkey'] = 2
food_dict['turkey'] = food_dict['turkey'] + 1

print(food_dict['pies'])
# print(food_dict['pizza']) ERROR

print('-------')

for key in food_dict:
    print(key)
print('-------')

for key in food_dict.keys():
    print(key)
print('-------')

for count in food_dict.values():
    print(count)
print('-------')

for food, count in food_dict.items():
    print(food, count)
