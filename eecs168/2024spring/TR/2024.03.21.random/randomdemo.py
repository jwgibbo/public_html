import random

print(random.randint(1, 20))

nums = [5, 10, 15, 20]
print(random.choice(nums))

words = ['bat', 'hat', 'cat', 'sat', 'mat']
print(random.choice(words))

print(random.choices(words, k=10))
print(random.sample(words, k=3))

random.shuffle(words)
print(words)
