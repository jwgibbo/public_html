def main():
    #open a file for reading
    poem_file = open("poem.txt", "r")
    grades_file = open("grades.txt", "r")
    avg_file = open("average.txt", "w")

    #read in the entire file
    #print(poem_file.read())

    #read in one line at a time
    for line in poem_file:
        print(line, end="")

    #Calculate the average grade
    grade_total = 0
    count = 0
    for grade in grades_file:
        grade_total = grade_total + int(grade)
        count = count + 1

    average = grade_total/count
    output_text = "Average grade: " + str(average)
    avg_file.write(output_text)

    poem_file.close()
    grades_file.close()
    avg_file.close()

main()
