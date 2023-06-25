###need to update this code not working correctly
students = []

while True:
    student = {}
    studentName = input("Please enter the student Name (or type 'report' to generate the summary): ")

    if studentName.lower() == 'report':
        break
    
    student["name"] = studentName
    subjects = []

    while True:
        subject = {}
        subjectName = input("Please enter the name of the subject: ")

        if not subjectName:
            break

        marks = int(input("Enter the marks for the subject: "))
        subject["name"] = subjectName
        subject["marks"] = marks
        subjects.append(subject)
    
    student["subjects"] = subjects
    student["totalMarks"] = sum([subject["marks"] for subject in subjects])
    student["percentageMarks"] = (student["totalMarks"] / (len(subjects) * 100)) * 100
    
    if student["percentageMarks"] >= 90:
        grade = "A"
    elif student["percentageMarks"] >= 60:
        grade = "B"
    elif student["percentageMarks"] >= 40:
        grade = "C"
    elif student["percentageMarks"] >= 20:
        grade = "D"
    else:
        grade = "F"

    student["grade"] = grade
    students.append(student)

print("\nSummary of Students (in descending order of grade):")

sorted_students = sorted(students, key=lambda x: x["grade"], reverse=True)

for student in sorted_students:
    print(f"Name: {student['name']}, Grade: {student['grade']}")
