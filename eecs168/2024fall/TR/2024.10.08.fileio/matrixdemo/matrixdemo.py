#matrixdemo.py

grid_file = open('datagrid.txt', 'r')

for line in grid_file:
    stripped_line = line.strip()
    split_line = stripped_line.split(' ')
    #iterate through the list of strings
    for string in split_line:
        number = int(string)
        print(number, end=' ')
    print('')

grid_file.close()
