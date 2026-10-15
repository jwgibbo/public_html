#stringtolist.py

candy_text = 'twix,m&ms,mars,zero,corn'
candy_list = candy_text.split(',')
print(candy_list)

delimiter = '$'
new_candy_text = delimiter.join(candy_list)
print(new_candy_text)

print('!'.join(candy_list))
