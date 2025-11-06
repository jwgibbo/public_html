my_tup = (5, 10, 15)
print(my_tup)
print(type(my_tup))
print('length =', len(my_tup))
var1, var2, var3 = my_tup #unpacks
print(var1, var2, var3)

print('----')
for num in my_tup:
    print(num)

print('----')
print(my_tup[0])
my_tup[0] = 99
