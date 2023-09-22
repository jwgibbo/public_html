#outputdemo.py

output_file = open('output.txt', 'w')
num = 82
output_file.write('Testing, testing\n')
output_file.write('Is this working?\n')
output_file.write(str(55)+'\n')
output_file.write(str(num)+'\n')

output_file.close()
