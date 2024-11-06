import random



for num in range(5):
    d20 = random.randint(1, 20)
    print(d20)

nums = [5, 10, 15, 20, 25, 30]
print(random.choice(nums))


menu = ['tacos', 'salads', 'sushi', 'fries', 'pizza']
selections = random.choices(menu, k=30)
print(selections)

food_sample = random.sample(menu, k=3)
print(food_sample)

random.shuffle(menu)
print(menu)
