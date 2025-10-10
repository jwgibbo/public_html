#filedemo.py

candy_file = open('candies.txt', 'r')

for line in candy_file:
    line = line.strip()
    if line == 'snickers':
        print('yay my favorite')

candy_file.close()

output_file = open('fallbreak.txt', 'w')
output_file.write('have a good \n BREAK')
output_file.close()
