import random

def main():

    roll_dice = random.randint(1, 6)
    print(roll_dice)

    menu = ['taco', 'pizza', 'salad', 'tuna', 'salmon']
    print(random.choice(menu))
    print(random.choices(menu, k=3))
    print(random.sample(menu, k=3))

    print(menu)
    random.shuffle(menu)
    print(menu)
    

main()
