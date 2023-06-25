from add import add
from multiply import multiply
from subtract import subtract
from divide import divide

# Get operator and inputs from the user
operator = input("Enter the operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the calculation based on the operator
result = None

if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = subtract(num1, num2)
elif operator == "*":
    result = multiply(num1, num2)
elif operator == "/":
    result = divide(num1, num2)
else:
    print("Error: Invalid operator!")

# Print the result
print("Your Result:", result)
