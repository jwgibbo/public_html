#Goal: Write a function that takes in an int and returns
#       one more than that number

def add_one(num):
    answer = num + 1
    return answer

def repeat_print(word, count):
    for num in range(count):
        print(word + '!')
        
def main():
    #Make a function call
    result = add_one(5)
    print(result)

    print(add_one(99))

    result = add_one(9) + add_one(19)
    print(result)

    repeat_print('banana', 3)

main() #entry point to our program
