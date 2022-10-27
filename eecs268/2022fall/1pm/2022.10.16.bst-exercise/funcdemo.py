def evil_func(num):
    num = 666

def main():
    x = 5
    evil_func(x)
    print(x) # x is 5
