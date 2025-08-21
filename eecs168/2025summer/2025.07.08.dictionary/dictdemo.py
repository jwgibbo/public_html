def main():
    bucket_dict = {}

    bucket_dict['paris'] = 4529
    bucket_dict['taipei'] = 7429
    bucket_dict['bali'] = 9622
    bucket_dict['sydney'] = 8838

    print(bucket_dict)
    print(len(bucket_dict)) #amount of key-value pairs
    print(bucket_dict['bali']) #prints value
    #print(bucket_dict['branson']) ERROR

    bucket_dict.pop('paris')
    print(bucket_dict)

    for city in bucket_dict.keys():
        print(city)

    print('-------------')

    for distance in bucket_dict.values():
        print(distance)

    print('-------------')

    for city, distance in bucket_dict.items():
        print(city, 'is', distance, 'miles away')

main()
    
    
