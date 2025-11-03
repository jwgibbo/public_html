dishes = {'ham': 9.2, 'pecan pie': 12, 'deviled eggs': 8.5}
print(dishes)
print('length =', len(dishes))

dishes['ham'] = 3.1
dishes['turkey'] = 5.0

if 'turkey' in dishes:
    print('turkey is in the dictionary')

print(dishes['ham'])
print('----')

for dish in dishes:
    print(dish, dishes[dish])

print('----')

for dish in dishes.keys():
    print(dish, dishes[dish])

print('----')

for rating in dishes.values():
    print(rating)

print('----')

for dish, rating in dishes.items():
    print(f'{dish} was rated {rating}')
