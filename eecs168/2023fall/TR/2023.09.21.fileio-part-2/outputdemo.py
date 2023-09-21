output_file = open('output.txt', 'w')

best_number = 14

output_file.write('Test string\n')
output_file.write('More text!\n')
output_file.write(str(55)+'\n')
output_file.write(str(best_number))

output_file.close()
