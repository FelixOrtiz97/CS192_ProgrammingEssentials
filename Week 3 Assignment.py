"""Program: Week 3 Assignment.py
Author: Felix Oritz
# Input field
1. Ask user to enter name
2. Ask user to enter 5 different values
# Calculations
1. Add the sum of the 5 values 
# statements
round all values to the first decimal
1. If the sum is greater than 0 print out the sum. (Your account balance is...)
2. If the sum is equal to 0 print out (Your account balance is 0)
3. If the sum is less than zero print out (Your account is overdrawn....)"""

# input field
input("Enter your name: ")
amount1 = float(input("Enter first amount: $"))
amount2 = float(input("Enter second amount: $"))
amount3 = float(input("Enter third amount: $"))
amount4 = float(input("Enter fourth amount: $"))
amount5 = float(input("Enter fifth amount: $"))

# Calculations
sum = amount1 + amount2 + amount3 + amount4 + amount5

# statements
if sum > 0:
    print("Your account balance is $%.1f"% + sum)
elif sum == 0:
    print ("Your account balance is 0")
elif sum < 0:
    print("Your account is overdrawn by $%.1f"% + sum)