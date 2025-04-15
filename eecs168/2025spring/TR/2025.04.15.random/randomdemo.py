import random

def main():
    d12 = random.randint(1, 12)
    print(d12)
    smells = ['popcorn', 'bbq', 'coffee', 'hospital', 'exhaust']
    print(random.choice(smells))
    print(random.choices(smells, k=10))
    print(random.sample(smells, k=3))

    print(smells)
    random.shuffle(smells)
    print(smells)

    

main()
