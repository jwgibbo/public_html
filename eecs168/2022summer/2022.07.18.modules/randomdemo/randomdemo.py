import random


def main():
    random_num = random.randint(1, 6)
    print(random_num)

    nums = [5, 10, 15, 20, 25, 30, 35]

    random_num = random.choice(nums)
    print(random_num)

    random_nums = random.choices(nums, k=20)
    print(random_nums)

    random_nums = random.sample(nums, k=99)
    print(random_nums)


main()
