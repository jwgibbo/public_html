#dictdemo.py

def main():
    grades = {}
    grades['john'] = 75
    grades['lisa'] = 94
    grades['homer'] = 88

    for key in grades.keys():
        print(key)

    print('----------')

    for value in grades.values():
        print(value)

    print('----------')

    for student, score in grades.items():
        print(student, score)
        
    grades.pop('john')
    print(grades)

    if 'john' in grades.keys():
        print(grades['john'])
    else:
        print('john is not in the class')
    

main()
