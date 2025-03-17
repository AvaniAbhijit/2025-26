# A for loop helps us repeat something again and again without writing the same code multiple times.
# The range() function helps us repeat something a fixed number of times in Python.
# range(1,5,1) on line 14 means "start at 1 and stop before 5 and increase by 1.
# The len() on line 23 helps us count how many items are in a list.
# range(5,1,-1) on line 18 means "start at 5 and stop before 1 and decrease by 1.


# Task 1: Run the code and observe the output.
# Task 2: Change the for loop range to print numbers till 5 for line 14.
# Task 3: Change the for loop range to print numbers till 0 for line 87.
# Task 4: Add 55 to the numbers list on line 22, run the code, and check the total.

print("Numbers 1 to 5")
for i in range(1,5,1):
    print(i)

print("Numbers 5 to 1")
for i in range(5,1,-1):
    print(i)

print("List creation")
numbers = [11,22,33,44]
total = len(numbers)

print("List items usingin operator in for loop")
for num in numbers:
    print(num)

print("Number in the list from index 0")
for i in range(total):
    print("index ",i, " - ", numbers[i])

print("Number in the list from last index")
for i in range(total - 1, -1, -1):
    print("index ",i, " - ", numbers[i])

