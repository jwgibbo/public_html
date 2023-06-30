#Function definition
def add_one(num):
    answer = num + 1
    return answer

def repeat_print(word, num_prints):
    for num in range(num_prints):
        print(word)
        


#Call the function
result = add_one(5)
print(result)

result = add_one(54)
print(result)

result = add_one(21) * 2

repeat_print('cookie', 27)
