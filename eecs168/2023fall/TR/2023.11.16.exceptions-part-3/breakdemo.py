
num = 0
while True:
    print(num)
    num += 1

    if num >= 5:
        break

print('----------')

for i in range(0, 51, 5):
    print(f'i={i}')
    for j in range(1000000):
        print(f'j={j}')
        if j >= 5:
            break
