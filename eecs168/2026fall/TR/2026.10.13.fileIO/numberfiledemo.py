#numberfiledemo.py

number_file = open('numbers.txt', 'r')

for number in number_file:
    number = int(number)
    print(number+1000)

number_file.close()
