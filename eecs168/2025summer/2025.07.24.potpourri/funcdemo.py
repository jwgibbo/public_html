def funky_town(a, b, c):
    print(f'a={a}')
    print(f'b={b}')
    print(f'c={c}')

def main():
    funky_town(5, 10, 15)
    funky_town(5, c=15, b=10)

main()
