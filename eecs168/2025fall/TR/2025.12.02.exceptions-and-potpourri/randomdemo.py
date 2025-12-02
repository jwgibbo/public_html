import random


def main():
    for num in range(10):
        roll = random.randint(1, 8)
        print(roll)

    weather = ['sunny', 'snow', 'rain', 'tornado']
    print(random.choice(weather))
    print(random.choices(weather, k=3))
    print(random.sample(weather, k=3))
    print(weather)
    random.shuffle(weather)
    print(weather)

main()
