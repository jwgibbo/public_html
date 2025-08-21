#Goal: Get numbers out of a file and add 10 to each
#Goal: Write the number+10s to a new file

num_file = open('nums.txt', 'r')
new_file = open('plus10.txt', 'w')

for number in num_file:
    print(int(number)+10)
    new_file.write(str(int(number)+10)+'\n')

num_file.close()
new_file.close()
