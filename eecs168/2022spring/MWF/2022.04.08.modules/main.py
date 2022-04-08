#main.py
import dice

def main():
    print("Here's your D6 result: ")
    print(dice.rollD6())

    print("Here's your D20 result ")
    print(dice.rollD20())

#call main
if __name__ == '__main__':
    main()
