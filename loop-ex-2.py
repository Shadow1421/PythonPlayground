# take starting and ending number from user and print all even numbers using loop in python
# and add Even and Odd numbers
startNumber = int(input("Enter the starting number: "))
endNumber = int(input("Enter the ending number: "))

sumOfEvenNumbers = 0
sumOfOddNumbers = 0

print("Even numbers between", startNumber, "and", endNumber, "are:")

for num in range(startNumber, endNumber+1):
    if num % 2 == 0:
        print(num)
        sumOfEvenNumbers += num
    else:
        sumOfOddNumbers += num


print("Sum of even numbers:", sumOfEvenNumbers)
print("Sum of odd numbers:", sumOfOddNumbers)
