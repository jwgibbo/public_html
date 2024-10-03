#fileIOdemo.py

candy_file = open('candy.txt', 'r')

for candy in candy_file:
    print(candy.strip())
