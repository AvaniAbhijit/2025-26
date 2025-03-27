# An if statement inside another if statement.

# Task1: Change the age value to 20 and check the output on line 7.
# Task2: Modify the code to include an else statement for the inner if condition (if age >= 21) on line 12.
# Note: For task 2, take care of indentation.

age = 25
if age >= 18:
    print("You can open a bank account.")
    if age >= 21:
        print("You are also eligible for a credit card.")

else: 
     print("You can not open a bank account.")

