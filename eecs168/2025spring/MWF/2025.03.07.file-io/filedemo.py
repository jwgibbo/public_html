vacation_file = open('vacation.txt', 'r')

for line in vacation_file:
    line = line.strip()
    print(line)

vacation_file.close()
