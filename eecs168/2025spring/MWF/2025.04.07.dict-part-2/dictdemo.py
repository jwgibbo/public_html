def main():
    candies = {}
    candies['peeps'] = 2
    candies['cadberry eggs'] = 10
    candies['jelly beans'] = 5.5
    candies['gummies'] = 10
    candies['cadberry eggs'] = 9.9
    
    if 'peeps' in candies:
        print('peeps is in there!')
    else:
        print('peeps is not in there')

    if 10 in candies:
        print('10 is in there!')
    else:
        print('10 is not in there')

    if 10 in candies.values():
        print('10 is in there!')
    else:
        print('10 is not in there') 
main()
