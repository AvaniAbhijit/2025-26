# This code defines a class Person with a constructor to set name and age,
# and two methods: greet and celebrate_birthday.
# Two objects person1 and person2 are created with different names and ages.
# The attributes (name and age) are accessed and printed directly.
# The methods greet and celebrate_birthday are called to show behavior based on the object's data.


#Task 1 : Create two more people: person4 with name "David" and age 28,
#        and person5 with name "Emma" and age 19. Call greet() and celebrate_birthday() on both.
# Task 2: Add a new method in the Person class called show_info() that prints:
#         Define a Person class with attributes name and age, and methods to greet and celebrate a birthday.

class Person:
  def __init__(self, name,age):
      self.name = name        # Initialize the name attribute
      self.age = age          # Initialize the age attribute

  def greet(self):
      print("Hello, my name is", self.name)  # Print greeting using the name

  def celebrate_birthday(self):
      self.age += 1  # Increase age by 1
      print("Happy birthday! I am now", self.age, "years old.")  # Print updated age

# Create two Person objects
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Access and print individual attributes
print(person1.name)  # Output: Alice
print(person2.age)   # Output: 30

# Call methods on the objects
person1.greet()  # Output: Hello, my name is Alice
person2.celebrate_birthday()  # Output: Happy birthday! I am now 31 years old
