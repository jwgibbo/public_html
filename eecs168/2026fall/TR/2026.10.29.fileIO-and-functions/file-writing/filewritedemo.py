costume_file = open('costumes.txt', 'w')

costume_file.write('D20\n')
costume_file.write('D21\n')
costume_file.write('bee\n')
costume_file.write('ninja\n')

num = 8
costume_file.write(str(num)+'-ball\n')

costume_file.write(f'That is a great {num}-ball\n')
costume_file.write(f'5*3+7={5*3+7}\n')
costume_file.close()
