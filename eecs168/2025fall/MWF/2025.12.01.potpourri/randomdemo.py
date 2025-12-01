import random

def main():
    for num in range(5):
        roll = random.randint(1, 20)
        print(roll)

    weather = ['snow', 'rain', 'sunny', 'tornado']

    print(random.choice(weather))
    print(random.choices(weather, k=3))
    print(random.choices(weather, k=8))
    print(random.sample(weather, k=3))

    print(weather)
    random.shuffle(weather)
    print(weather)

main()
