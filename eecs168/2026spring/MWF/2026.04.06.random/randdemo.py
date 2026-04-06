import random

def main():
    d20 = random.randint(1, 20)
    d6 = random.randint(1, 6)

    print(d20)
    print(d6)

    nums = [5, 10, 15, 20, 25, 30]
    print(random.choice(nums))

    menu = ['pizza', 'tacos', 'salad', 'burger']
    print(random.choices(menu, k=3))
    print(random.sample(menu, k=3))

    random.shuffle(nums)
    print(nums)

    

main()
