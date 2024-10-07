#numberdemo.py

number_file = open('data.txt', 'r')
double_file = open('double.txt', 'w')

for line in number_file:
    num = int(line.strip())
    print(num+2)
    double_file.write(str(num+2)+'\n')

number_file.close()
double_file.close()
