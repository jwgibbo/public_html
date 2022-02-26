#Goal: Define a function that takes a
#      number and returns that number
#      plus one

def add_one(num):
    #You can use all your tools
    #in a function definition
    answer = num + 1
    return answer

#Define a function that takes two
#numbers and returns the larger
def cool_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

#Goal: Define a function that takes in
#       a number then print the word
#       "Galapagos" num times
def galapagos(num):
    for _ in range(num):
        print("Galapagos")

def main():
    num = 5
    #the parameter num gets a value
    #when we call add_one
    one_more = add_one(num)
    print(num)
    print(one_more)
    print(cool_max(3, 91))
    galapagos(1000)

#call main
main()
