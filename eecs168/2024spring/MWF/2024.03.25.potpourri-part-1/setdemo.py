my_word = 'pizza'
your_word = 'zipper'

my_set = set(my_word)
print(my_set)

your_set = set(your_word)
print(your_set)

print(my_set.intersection(your_set))
print(my_set.union(your_set))
print(my_set.difference(your_set))
print(your_set.difference(my_set))
