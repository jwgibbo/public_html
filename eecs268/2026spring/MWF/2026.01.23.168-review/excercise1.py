def odd_count(nums):
    count = 0

    for num in nums:
        if num % 2 == 1: #is num odd?
            count = count + 1

    return count

def main():
    values = [5, 2, 24, 17, 3, 6, 0, 33, 11, 9]
    print(odd_count(values))

main()
