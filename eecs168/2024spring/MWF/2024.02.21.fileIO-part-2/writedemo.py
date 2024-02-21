output_file = open('output.txt', 'w')
output_file.write('testing, testing\n')
output_file.write('is this thing on?\n')

base = float(input('Enter a base: '))
height = float(input('Enter a height: '))
area = base*height*0.5
output_file.write(str(base) + '*' + str(height) + ' * 0.5 = ' + str(area) + '\n')
output_file.write(f'{base}*{height}*0.5 = {area}\n')

output_file.close()
