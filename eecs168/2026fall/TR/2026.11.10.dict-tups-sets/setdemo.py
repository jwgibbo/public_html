my_letters = set('banana')

print(my_letters)

my_letters.add('z')
my_letters.add('q')


print(my_letters)

your_letters = set('pizza')
print(my_letters.intersection(your_letters))


words = ['bat', 'cat', 'bat', 'hat', 'mat', 'cat']

unique_words = set(words)
print(unique_words)
