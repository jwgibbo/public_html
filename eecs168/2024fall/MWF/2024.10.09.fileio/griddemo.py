#griddemo.py

numbers_file = open('data.txt', 'r')

#go through all the lines
for line in numbers_file:
    line = line.strip()
    list_of_strings = line.split(' ')
    print(list_of_strings)
    #go through each string and cast it!
    for string in list_of_strings:
        num = int(string)
        print(num*2)
    

numbers_file.close()
