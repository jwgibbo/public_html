import random

def main():
    d20_roll = random.randint(1, 20)
    d6_roll = random.randint(1, 6)

    print(d20_roll)
    print(d6_roll)

    menu = ['taco', 'fish', 'salad', 'beef']
    print(random.choice(menu))
    print(random.choices(menu, k=5))
    print(random.sample(menu, k=3))
    random.shuffle(menu)
    print(menu)


main()
