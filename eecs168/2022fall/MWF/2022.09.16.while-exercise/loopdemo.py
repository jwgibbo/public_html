word = input('Enter a word: ')
count = 0

#count the A's in the word
for letter in word:
    if letter == 'a' or letter == 'A':
        count = count + 1

print("There are", count, "A's in the word")
