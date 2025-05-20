# The code demonstrates inheritance in Python using classes.
# A base class Animal is defined, and a derived class Dog inherits from it using the syntax class Dog(Animal).
# An animal has: An __init__ method (constructor) to store the name. A method sound() that prints a generic message: "Animal makes a sound".
# Dog inherits the __init__ method from Animal (so it doesn't need its own).
# It overrides the sound() method to give a custom behavior: prints "Buddy says Woof!" (or any other name passed).
# An Animal object a is created, and it uses the base class method.
# A Dog object d is created, and it uses the overridden sound() method.

# Inheritance: Dog class inherits properties and methods from Animal.
# Method Overriding: Dog class overrides the inherited method to customize behavior.
# Object Creation and Method Calling: Shows how objects use the correct method based on their class.

import pygame

# Create a base class (just like Sprite)
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound")

# Create a derived class (inherits from Animal)
class Dog(Animal):
    def sound(self):
        print(f"{self.name} says Woof!")

# Using the classes
a = Animal("AnyAnimal")
a.sound()     # Output: Animal makes a sound

d = Dog("Buddy")
d.sound()     # Output: Buddy says Woof!

