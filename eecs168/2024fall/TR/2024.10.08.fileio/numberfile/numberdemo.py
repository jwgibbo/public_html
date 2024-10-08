#numberdemo.py

#open the file
number_file = open('data.txt', 'r')

#open a file for writing
squares_file = open('squares.txt', 'w')

for line in number_file:
    number = int(line.strip())
    print(number**2)
    squares_file.write(f'{number**2}\n')


#close the files
number_file.close()
squares_file.close()
