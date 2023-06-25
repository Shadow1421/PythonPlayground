studentNames = []
mathMarksList = []
scienceMarksList = []
englishMarksList = []
totalMarksList = []
percentageMarksList = []
studentDataList = []

flag = "y"
while flag == "y":
    studentName = input("Please enter the student Name: ")
    studentNames.append(studentName)

    # Validation logic
    mathMarks = int(input("Please enter the marks for Math: "))
    mathMarksList.append(mathMarks)
    scienceMarks = int(input("Enter the marks for Science: "))
    scienceMarksList.append(scienceMarks)
    englishMarks = int(input("Enter the marks for English: "))
    englishMarksList.append(englishMarks)

    # Processing the marks
    totalMarks = mathMarks + scienceMarks + englishMarks
    totalMarksList.append(totalMarks)
    print("The total marks of the student would be ", totalMarks)

    # Percentage of the total marks
    percentageMarks = (totalMarks / 300) * 100
    percentageMarksList.append(percentageMarks)

    # Grade calculation
    if percentageMarks >= 90:
        grade = "A"
    elif percentageMarks >= 60 and percentageMarks < 90:
        grade = "B"
    elif percentageMarks >= 40 and percentageMarks < 60:
        grade = "C"
    elif percentageMarks >= 20 and percentageMarks < 40:
        grade = "D"
    else:
        grade = "E"

    # Add grade to the student's data
    studentData = (studentName, grade)
    studentDataList.append(studentData)

    flag = input("Do you have any other student data? (y/n) ")

# Sort students based on grade
sortedStudents = sorted(studentDataList, key=lambda x: x[1])

print("Students arranged based on their grades:")
for student in sortedStudents:
    print(student[0], " - Grade:", student[1])
