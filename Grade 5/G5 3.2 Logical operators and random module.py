# Logical operators - and/or - help to combine 2 conditions.
# For the 'and' logical operator: Both conditions must be true. 
# For the 'or' logical operator: Any one condition can be true.
# The program below checks if the number is between the range 10 and 50 on line 14.


# Task 1: Run the program and check the output.
# Task 2: Change the num variable value to 55 on line 11 and run to see the output.
# Task 3: Change 'and' operator to 'or' and now run and see the output.

num = 25

# and operator is joining 2 conditions - num>=10 and num<=50
if num >= 10 and num <= 50:
    print("The number is found!")   # both conditions must be true to print this statement

