import os

# Check if the file exists
if os.path.isfile("employee.txt"):
    # Open the file in read mode
    with open("employee.txt", "r") as file:
        # Read the contents of the file
        contents = file.read()
        
        # Display the contents
        print("Existing Employee Data:")
        print(contents)

# Prompt the user for inputs
name = input("Enter employee name: ")
department = input("Enter department: ")
salary = input("Enter salary: ")

# Open the file in append mode to add new data
with open("employee.txt", "a") as file:
    # Write the user inputs to the file
    file.write(f"\n{name}, {department}, {salary}")

# Open the file again to read the updated contents
with open("employee.txt", "r") as file:
    # Read the contents of the file
    contents = file.read()

# Display the complete data from the file
print("\nUpdated Employee Data:")
print(contents)
