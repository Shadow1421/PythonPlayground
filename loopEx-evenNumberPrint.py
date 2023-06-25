#program to print all even number in range when last number is selected by user
#############################
#using addition method
number = int(input("Please enter a number: "))
sumValue = 0

print("Even numbers are: ")
for index in range(2, number+1, 2):
    print(index)
    sumValue += index

print("Sum of even numbers: ", sumValue)


#############################
# #using reminder method
# Take input from the user
number = int(input("Enter a number: "))

# Initialize variables
sumValue = 0

# Print all even numbers and calculate their sum
print("Even numbers are: ")
for index in range(1, number + 1,1):
    if index % 2 == 0: 
        print(index)
        sumValue += index

# Display the even numbers and their sum
print("Sum of even numbers: ", sumValue)
