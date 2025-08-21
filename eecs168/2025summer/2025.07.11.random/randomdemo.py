import random

def main():
    roll = random.randint(1, 6)
    print(roll)

    nums = [5, 10, 15, 20, 25, 30]
    print(random.choice(nums))
    print(random.choices(nums, k=3))
    print(random.sample(nums, k=3))
    random.shuffle(nums)
    print(nums)

main()
    
    
