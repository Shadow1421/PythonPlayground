def calculate_power(base, power):
    result = base ** power
    return result

def get_positive_input(prompt):
    while True:
        try:
            num = float(input(prompt))
            if num > 0:
                return num
            else:
                print("Invalid input. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

base_num = get_positive_input("Enter the base number: ")
power_num = get_positive_input("Enter the power number: ")

result = calculate_power(base_num, power_num)
print(f"The result of {base_num} raised to the power of {power_num} is: {result}")

# Save the result to a file
filename = "result.txt"
with open(filename, "w") as file:
    file.write(f"The result of {base_num} raised to the power of {power_num} is: {result}")

print("Result saved to file:", filename)
