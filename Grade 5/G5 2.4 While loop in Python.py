# A loop in Python is used when you need to repeat the same action.
# The while loop executes as long as the condition is not met.
# Note the indentation(spacing) within while loop on lines 18 and 19.
# In the example below, the loop keeps running as long as the number of chocolates is more than 0.

# Task 1: Press the backspace key to remove the space before the line on 19. 
#        Run the code and observe the output. Why is this happening?

# Task 2: Write a while loop to print numbers from 1 to 5 on line 24.
#         Hint: Use the condition number < 6 for the while loop.

# Task 3: Uncomment lines 27 and 28. What do you see?
#        This is an infinite loop as the condition is always True.

chocolates = 5  # You have 5 chocolates

while chocolates > 0:  # While you still have chocolates
    print("Eating one chocolate!")
    chocolates = chocolates - 1  # Reduce the number of chocolates

print("No more chocolates left!")

number = 1



#while True:
#    print("Eating one chocolate!")

