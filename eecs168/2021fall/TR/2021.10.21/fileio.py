def main():
    #open the file
    grade_file = open("grades.txt", "r")
    avg_file = open("average.txt", "w")
    
    grade_total = 0
    count = 0
    #read each line from file
    for line in grade_file:
        print(line, end="")
        grade_total = grade_total + int(line)
        count = count + 1

    average = grade_total/count
    avg_file.write(str(average))    
    

main()
