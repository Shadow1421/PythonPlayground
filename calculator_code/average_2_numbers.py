def calculate_average(n, m):
    average = (n + m) / 2
    return average

while True:
    try:
        # Prompt the user to enter two numbers (N and M)
        n = float(input("Enter the first number (N): "))
        m = float(input("Enter the second number (M): "))

        # Check if the entered numbers satisfy the condition
        if 1 <= n <= 1000 and 1 <= m <= 1000:
            # Calculate the average
            result = calculate_average(n, m)
            # Print the average with 4 decimal places
            print("{:.4f}".format(result))
            break
        else:
            print("Invalid input. Numbers should satisfy the condition 1≤N,M≤1000.")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
