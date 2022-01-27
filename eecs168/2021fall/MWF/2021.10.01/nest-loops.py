
print("Let's play with nested loops")
for i in range(1,4):
    for j in range(1,5):
        print(f"{i-j}", end=",")


print("Now let's play with a matrix")
matrix = [[1,2,3,4], [2,4,6,8], [3,6,9,12]]

print(f"matrix={matrix}")

for row in matrix:
    for num in row:
        print(num)


