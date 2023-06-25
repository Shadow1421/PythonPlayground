# take starting and ending number from user and print all numbers using loop in python
# and add those numbers
startNumber = int(input("Enter the starting number: "))
endNumber = int(input("Enter the ending number: "))

sumNumbers = 0

for num in range(startNumber, endNumber + 1):
    print(num)
    sumNumbers += num

print("Sum of the numbers:", sumNumbers)
