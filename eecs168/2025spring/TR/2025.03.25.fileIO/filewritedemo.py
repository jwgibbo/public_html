todo_file = open('todo.txt', 'w')

todo_file.write('lab eval\n')
todo_file.write('relax\n')
todo_file.write('grading\n')
num = 5
todo_file.write(f'The answer is {num}\n')

todo_file.close()
