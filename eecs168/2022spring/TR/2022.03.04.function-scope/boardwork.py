def main():
    year = int(input('Enter a year'))

    if is_valid_year(year):
        if is_leap_year(year):
            print("It's a leap year!")
        else:
            print("It's not a leap year")
    else:
        print("Year must be positive")
