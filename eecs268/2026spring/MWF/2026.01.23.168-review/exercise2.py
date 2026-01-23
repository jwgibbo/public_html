def sum_from_file(filename):
    num_file = open(filename, 'r')
    total = 0
    
    for line in num_file:
        total += int(line.strip())

    num_file.close()

    return total

def main():
    print(sum_from_file('data.txt'))

main()
