import random

def main():
    print(random.randint(1, 20))

    events = ['soccer', 'pinball', 'work', 'read', 'fishing', 'sleep']
    print(random.choice(events))
    print(random.choices(events, k=3))
    print(random.sample(events, k=3))
    print(events)
    random.shuffle(events)
    print(events)
    
    

main()
