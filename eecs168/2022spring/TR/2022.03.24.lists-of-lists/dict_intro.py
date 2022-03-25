def main():

    #Let's store some grades
    list_of_grade = [99, 78, 83, 45]

    #make an empty dict
    grades = {}

    grades['john'] = 45
    grades['alex'] = 99
    grades['molly'] = 100
    grades['chimichumi'] = 90

    #Print all the grades
    for student, grade in grades.items():
        print(student + ' got a ' + str(grade))
    

main()
