# A list in Python is like a box that can hold many things together.
# You can keep numbers, words, or a mix of both inside a list.
# We can make a list by using square brackets [ ] and putting items inside, separated by commas.
# The .append() function is used to add an item to the end of a list.
# The .clear() function is used to remove all items from the list, making it empty.
# On line 25, New_fruits is an empty list created using [].
# Each item in a list has a position number called an index. Python starts counting from 0 (not 1!).

# Task1: Create a new list of your favorite colors on line 35 and print it.
# Task 2: Add a new color to the list using .append() and print the updated list.
# Task3: Remove all items from the list using .clear() and print the empty list.
# Task4: Create a list of 5 numbers and print the third number using indexing.


# Here, fruits is a list that contains three items: apple, banana, and cherry
fruits = ["apple", "banana", "cherry"]
print(fruits)

fruits.append("Mango") # The .append() function is used to add an item to the end of a list.
print("After appending Mango:",fruits)

fruits.clear() # The .clear() function is used to remove all items from the list, making it empty.
print("After clearing list:",fruits)

New_fruits =[]          # empty list
print("Empty list:",New_fruits)
New_fruits.append("apple")
New_fruits.append("banana")
New_fruits.append("cherry")
print("List after append the fruits:",New_fruits)
print("First fruit _index 0 in the list:",New_fruits[0])  # First item
print("Second fruit _index 1 in the list:",New_fruits[1])  # Second item
print("Third fruit _index 2 in the list:",New_fruits[2])  # Third item
