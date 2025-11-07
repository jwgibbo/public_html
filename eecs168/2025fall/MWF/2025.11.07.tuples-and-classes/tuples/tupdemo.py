#tupdemo.py
my_tup = (5, 10, 15)
print(my_tup)
print(my_tup[0])
print('length =', len(my_tup))
# my_tup[0] = 99   ERROR

a, b, c = my_tup
print('a=', a)
print('b=', b)
print('c=', c)
print(my_tup)

print('-------')
for num in my_tup:
    print(num)
print('-------')
