import os

def read_employee_data():
    # Check if the file exists
    if os.path.isfile("employee.txt"):
        # Open the file in read mode
        with open("employee.txt", "r") as file:
            # Read the contents of the file
            contents = file.read()

            # Display the contents
            print("Existing Employee Data:")
            print(contents)

def add_employee_data():
    # Prompt the user for inputs
    name = input("Enter employee name: ")
    department = input("Enter department: ")
    salary = input("Enter salary: ")

    # Open the file in append mode to add new data
    with open("employee.txt", "a") as file:
        # Write the user inputs to the file
        file.write(f"\n{name}, {department}, {salary}")

def display_employee_data():
    # Open the file in read mode
    with open("employee.txt", "r") as file:
        # Read the contents of the file
        contents = file.read()

        # Display the complete data from the file
        print("\nUpdated Employee Data:")
        print(contents)

def search_employee_data():
    # Read the contents of the file
    with open("employee.txt", "r") as file:
        contents = file.read()

    # Prompt the user to enter a name for searching
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

# Main program flow
def main():
    read_employee_data()
    add_employee_data()
    display_employee_data()
    search_employee_data()

# Call the main function to start the program
main()
