import random

d20 = random.randint(1, 20)
print(d20)

print('----------')

classes = ['paladin', 'mage', 'cleric', 'thief', 'fighter', 'bard', 'ranger', 'druid']
print(random.choice(classes))

party = random.choices(classes, k=4)
print(party)

unique_party = random.sample(classes, k=4)
print(unique_party)

nums = [5, 10, 15, 20, 25, 30]
random.shuffle(nums)
print(nums)

random_rolls = random.choices(range(1,21), k=3)
print(random_rolls)
