# import random on line 8 module used to generate random numbers.
# random.randint(1,50) on line 9 generates a random integer between 1 and 50 (inclusive).


# Task 1: Change 50 on line 9 to some other number. Run and see the output.
# Task 2: Write an if statement on line 13 to check if secret_number < 30. If so, print("Yes it is")

import random
secret_number = random.randint(1, 50)
print(secret_number)

# check if secret_number < 30. If so, print("Yes it is")
