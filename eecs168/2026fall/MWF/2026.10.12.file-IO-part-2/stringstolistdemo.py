candy_text = 'snickers,twix,mars,bit-o-honey'
print(list(candy_text))

candy_list = candy_text.split(',')
print(candy_list)

delimiter = '$'

joined_candy = delimiter.join(candy_list)
print(joined_candy)
