#Create a program that a score from the user
#and output a letter grade
#RULE: No using elif (other forms of if ok)

score = float(input('Enter your score: '))

if score >= 90:
    print('A')

if score >= 80 and score < 90:
    print('B')

if score >= 70 and score < 80:
    print('C')

if score >= 60 and score < 70:
    print('D')

if score < 60:
    print('F')
