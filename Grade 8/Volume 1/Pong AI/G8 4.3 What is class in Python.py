# Task Create person3 and call celebrate_birthday on this object.
class Person:
  def __init__(self, name,age):
      self.name = name
      self.age = age

  def greet(self):
      print("Hello, my name is", self.name)

  def celebrate_birthday(self):
      self.age += 1
      print("Happy birthday! I am now", self.age, "years old.")

# Creating instances (objects) of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Accessing attributes
print(person1.name)  # Output: Alice
print(person2.age)   # Output: 30

# Calling methods
person1.greet()  # Output: Hello, my name is Alice
person2.celebrate_birthday()  # Output: Happy birthday! I am now 31 years old
