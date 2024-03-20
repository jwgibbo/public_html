def main():
    word = 'abc'*100000
    print(word)

    letter_counts = {}

    for letter in word:
        if letter in letter_counts.keys():
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    print(letter_counts)

main()
