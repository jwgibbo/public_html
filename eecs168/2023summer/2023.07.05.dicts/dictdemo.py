def main():
    grades = {} #empty dict
    grades['john'] = 73
    grades['rowdy'] = 88
    grades['kitner'] = 94

    print(grades)
    print(len(grades))

    for student, grade in grades.items():
        print(student, 'got a/an', grade)

main()
