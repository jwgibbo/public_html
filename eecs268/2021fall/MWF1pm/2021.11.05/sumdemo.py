import specialsum

def main():
    print("Welcome user!")
    print("Watch me sum up these values!")

    nums = [10, 15, -20, 44, -88]

    print("I'll add all the positive values")
    print(nums)
    print("Sum = ", specialsum.sum_positives(nums))
    print("Okay bye!")

if __name__ == "__main__":
    main()
