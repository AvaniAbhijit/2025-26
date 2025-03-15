# Logical operators - and / or - help to combine 2 conditions.
# For 'and' operator: Both conditions must be true. For 'or' operator: Anyone condition can be true.
# Below program checks if the number is between the range 10 and 50

# import random on line 14: module used to generate random numbers.
# random.randint(1,10) on line 21: Generates a random integer between 1 and 10 (inclusive)

# Task 1: Run the program and check the output.
# Task 2: Change the num value to 55 on line 14 and run to see the output.
# Task 3: Change 'and' operator to 'or' and now run and see the output.
# Task 4: Change 10 on line 21 to some other number. Run and see the output.
# Task 5: Write an if statement on line 23 to check if secret_number < 30. If so, print("Yes it is")

import random
num = 25

# and operator is joining 2 conditions - num>=10 and num<=50
if num >= 10 and num <= 50:
    print("The number is found!")   # both conditions must be true to print this statement

secret_number = random.randint(1, 10)
print(secret_number)
