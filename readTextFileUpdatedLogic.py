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

# Search for a user's data
search_name = input("\nEnter the employee name to search: ")

# Check if the user's data exists in the file
if search_name in contents:
    print(f"\nFound Employee Data for {search_name}:")
    
    # Split the contents into individual lines
    lines = contents.split("\n")
    
    # Iterate over the lines to find the matching data
    for line in lines:
        if search_name in line:
            print(line)
else:
    print(f"\nEmployee Data for {search_name} not found.")
