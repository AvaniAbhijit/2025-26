# The if statement runs code only if the condition is True means when the age is greater than 18.
# The else block runs when the condition is False, which means when the age is less than 18.
# Observe the indentation(spacing) of the code within the if and else block on lines no.11 & 13.
# Relational operators(==, !=, >, <, >=, and <=.)are used in the condition, observed on line no 9.

# Task: Write the if statement to check num = 7 is an odd number or an even number.
# Hint: Use num % 2 == 0 as the if condition.

age = 16
if age >= 18:
    print("You can vote!")
else:
    print("You cannot vote.")
print("-------------------------")
# The or operator checks any one condition is true, it prints: "You can vote!"

age = 16
if age > 18 or age==18:
    print("You can vote!")
else:
    print("You cannot vote.")
print("-------------------------")

# The and operator checks both conditions are True, it prints: "You can vote!"

age = 20  
citizen = True  

if age >= 18 and citizen:  
    print("You can vote!")  
else:  
    print("You cannot vote.") 
