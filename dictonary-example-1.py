# Create if list of dictionary, where ask name and marks from user until he ask for report generation
# In report generation show which student pass or not
# passing marks is 35
students = []

while True:
    name = input("Enter student name (or type 'report' for report generation): ")
    
    if name.lower() == 'report':
        break
    
    marks = int(input("Enter marks: "))
    
    student = {'name': name, 'marks': marks}
    students.append(student)

print("\nReport Generation:")

for student in students:
    if student['marks'] >= 35:
        result = "Pass"
    else:
        result = "Fail"
    
    print(f"Name: {student['name']}, Marks: {student['marks']}, Result: {result}")
