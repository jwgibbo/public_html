def main():
    nums = [5, 10, 15, 20, 25, 30, 35, 40]
    cubes = [num**3 for num in nums]
    odd_cubes = [num**3 for num in nums if num%2==1]
    print('nums =', nums)
    print('cubes =', cubes)
    print('odd cubes =', odd_cubes)


main()
