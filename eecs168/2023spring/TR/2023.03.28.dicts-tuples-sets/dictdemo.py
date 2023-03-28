#Goal: Define a function that takes a dictionary
#       as a parameter. Assume the dictionary is
#       filled with student names and their grade
#       Give every student 100 bonus points

def bonus(grade_book):
    for student, grade in grade_book.items():
        grade_book[student] = grade + 100



def main():
    grade_book = {} #empty dict
    grade_book['john'] = 65.5
    grade_book['lisa'] = 98.1
    grade_book['chimichumi'] = 55.5

    print(grade_book)

    bonus(grade_book)

    print(grade_book)

    #move the value at key 'john' to key 'jack'
    grade_book['jack'] = grade_book['john']
    grade_book.pop('john') #remove old key-value pair

main()
