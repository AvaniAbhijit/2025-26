# The while loop is used when you want to repeat instructions until a condition is false.
# True and False are Boolean values.

# Task 1: Run the code and observe the output.
# Task 2: Change the code to print the numbers in reverse order from 20 to 1 using a while loop.

running = True
num = 0
while running:
    num = num + 5
    print(num, " in while loop")
    if num > 20:
        running = False
print("done running while loop")
