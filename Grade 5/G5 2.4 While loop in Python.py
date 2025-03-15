# A loop is used when you need to repeat the same action.
# While loop executes as long as the condition is not met.
# Note the indentation(spacing) within while loop on the lines 18 and 19.
# In the below example, the loop keeps running as long as chocolates are more than 0.

# Task 1: Move the line 'chocolates = chocolates - 1' back -> in line with while.
#        Run the code and observe the output. Why is it happening so?

# Task 2: Write a while loop to print numbers from 1 to 5 on line 24.
#         Hint: use the condition number < 6 for the while loop.

# Task 3: Uncomment lines 27 and 28. What do you see ?
#        This is an infinte loop as the condition is always True.

chocolates = 5  # You have 5 chocolates

while chocolates > 0:  # While you still have chocolates
    print("Eating one chocolate!")
    chocolates = chocolates - 1  # Reduce the number of chocolates

print("No more chocolates left!")

number = 1



#while True:
#    print("Eating one chocolate!")

