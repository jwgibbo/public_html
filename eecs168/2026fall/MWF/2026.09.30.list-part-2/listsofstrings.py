words = []

words.append('bird')
words.append('dog')
words.append('cat')
words.append('fish')

print('length =', len(words))
print(words)
for word in words:
    print(word[0])

print(type(words[0]))
print(words[0][0])
print('-------')
for word in words:
     for letter in word:
         print(letter)
