word1 = 'banana'
word2 = 'naples'
letters1 = set(word1)
letters2 = set(word2)

print(letters1)
print(letters2)

intersection = letters1.intersection(letters2)
print(intersection)

union = letters1.union(letters2)
print(union)

difference1 = letters1.difference(letters2)
print(difference1)

difference2 = letters2.difference(letters1)
print(difference2)

your_words = ['bruh', 'POV', 'dab', 'cool', 'chill']
my_words = ['tarnashun', 'jolly jeepers', 'cool', 'gorsh']

your_set = set(your_words)
my_set = set(my_words)
print(your_set)
print(my_set)
