import random

def main():
    for num in range(10):
        dice_roll = random.randint(1, 6)
        print(dice_roll)

    menu = ['pizza', 'taco', 'sloppy joe', 'salad', 'salmon']
    print(random.choice(menu))
    print(random.choices(menu, k=3))
    print(random.sample(menu, k=3))

    print('before shuffle', menu)
    random.shuffle(menu)
    print('post shuffle', menu)

main()
    
