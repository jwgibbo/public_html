#setdemo.py

number_set = {5, 10, 15}
print(number_set)
number_set.add(99)
print(number_set)
number_set.add(5)
print(number_set)

letters = set('banana')
print(letters)

letters2 = set('argonaut')
print(letters2)

print(letters.intersection(letters2))
print(letters.difference(letters2))
print(letters2.difference(letters))
print(letters.union(letters2))
