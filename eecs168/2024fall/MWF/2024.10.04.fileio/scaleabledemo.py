nums = []
amount = 5000
for i in range(amount):
    user_num = int(input('Enter a num: '))
    nums.append(user_num)


grid = []
num_rows = 50
num_cols = 60
for row in range(num_rows):
    current_row = []
    for col in range(num_cols):
        user_num = int(input('Enter num: '))
        current_row.append(user_num)
    grid.append(current_row)
