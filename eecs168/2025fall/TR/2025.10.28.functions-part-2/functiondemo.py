#Goal: Define a function that takes in
#       a number and returns one more
#       than that number
def one_up(num):
    #you don't need to give num a value
    answer = num + 1
    #you don't need to print
    return answer

def main():
    answer = 99
    result = one_up(4)
    print(result)
    print("main's answer =", answer)

main() #only command NOT inside a function
