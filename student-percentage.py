studentNames = []
mathMarksList = []
scienceMarksList = []
englishMarksList = []
totalMarksList = []
percentageMarksList = []

flag = "y"
while (flag == "y"):
    studentName = input("Please enter the student Name:")
    studentNames.append(studentName)
# validation logic
    mathMarks = int(input("Please enter the marks for Math"))
    mathMarksList.append(mathMarks)
    scienceMarks = int(input(" Enter the marks for Science"))
    scienceMarksList.append(scienceMarks)
    englishMarks = int(input(" Enter the marks for English"))
    englishMarksList.append(englishMarks)

# Processing the marks
    totalMarks = mathMarks+scienceMarks+englishMarks
    totalMarksList.append(totalMarks)
    print(" The total marks of the student would be ", totalMarks)

# percentage of the total marks
    percentageMarks = (totalMarks/300)*100
    percentageMarksList.append(percentageMarks)
#####
# if statement
    if (percentageMarks < 30):
        print(" The student have failed")
        print(" grade : F")
    elif (percentageMarks < 60):

        print("Grade D")

    elif (percentageMarks < 80):

        print("grade A")
    else:
        print("grade E")
    flag = input("do you have any other student data y/n")

#logic to show highest % student
highestPercentageUserIndex = percentageMarksList.index(max(percentageMarksList))

print("Class topper is", studentNames[highestPercentageUserIndex], "with", round(percentageMarksList[highestPercentageUserIndex]))