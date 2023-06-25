# #simple interest calculation
# # A = p(1 + rt)
# # A => Final amount 
# # p => initial principle balance #Input from user
# # r => annual interest rate #fixed - r/i - 5%
# # t => time (in years) #Input from user 

# #Fetch principle amount from user
# p = int(input("Please enter loan amount: "))
# t = int(input("Please enter tenure(in years) of loan: "))
# r = float(5/100) # Rate of interest in %

# #check if principle or time should be greater than 0
# if p <= 0:
#     print("principle amount should be greater than 0")
# elif t <= 0:
#     print("Loan tenure(in years) should be greater than 0")
# else:
#     A = p * (1 + r*t)
#     print("your final loan amount will be: ", A)
#     emi = round(A / (t * 12),2)
#     print("Your EMI will be: ", emi)


my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

del my_dict['age']

print(my_dict)