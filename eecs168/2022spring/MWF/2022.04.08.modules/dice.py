#dice.py
import random

def rollD6():
    return random.randint(1, 6)

def rollD20():
    return random.randint(1, 20)

def main():
    print('dice module is just a helper module')

if __name__ == '__main__':
    main()
