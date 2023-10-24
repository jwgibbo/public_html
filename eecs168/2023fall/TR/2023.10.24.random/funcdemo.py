def repeat_print(word='DEFAULT', amount=1):
    for num in range(amount):
        print(word)

def main():
    repeat_print('banana')
    repeat_print('frog', 5)
    repeat_print()

main()
