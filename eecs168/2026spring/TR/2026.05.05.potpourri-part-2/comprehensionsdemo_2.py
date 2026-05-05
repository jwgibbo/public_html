def main():
    nums = [5, 10, 15, 20, 25]
    cubes = [num**3 for num in nums]
    odds = [num for num in nums if num%2==1]

    print('nums =', nums)
    print('cubes =', cubes)
    print('odds =', odds)

main()
