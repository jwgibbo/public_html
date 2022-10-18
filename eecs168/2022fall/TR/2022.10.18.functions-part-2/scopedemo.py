def evil_func(num):
    print(num)
    num = -1
    print(num)
    print("Muahahaha!")

def main():
    num = 5
    print(num)
    evil_func(num)
    print(num)

main()
