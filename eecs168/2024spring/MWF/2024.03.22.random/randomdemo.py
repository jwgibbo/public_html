import random

roll = random.randint(1, 20)
print(roll)

teams = ['KU', 'LSU', 'Illinois', 'Oakland', 'Gonzaga']
print(random.choice(teams))

menu = ['burrito', 'pancakes', 'tacos', 'beer', 'waffles']
print(random.choices(menu, k=10))
print(random.sample(menu, k=3))

print(menu)
random.shuffle(menu)
print(menu)
