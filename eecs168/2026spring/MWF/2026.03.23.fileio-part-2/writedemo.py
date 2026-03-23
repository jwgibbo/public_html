#writedemo.py

destinations_file = open('springbreak.txt', 'w')
num = 55
destinations_file.write('San Diego\n')
destinations_file.write('Kansas City\n')
destinations_file.write('Costa Rica\n')
destinations_file.write('Backyard\n')
destinations_file.write(str(num)+'\n')
destinations_file.write(str(num+1)+'\n')
destinations_file.close()
