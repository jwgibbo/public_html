#fileiodemo.py

file_name = 'fireworks.txt'

#open the file
fireworks_file = open(file_name, 'r')

#copy of the file
copy_file = open('copy.txt', 'w')

for line in fireworks_file:
    line = line.strip()
    print(line)
    copy_file.write(line + '\n')


#Final act, close all files
fireworks_file.close()
copy_file.close()
