# Base Class: Animal
# Derived Class: Dog
# Derived class inherits from Animal using the syntax - class Dog(Animal).
# Animal class has a method sound() that prints: "Animal makes a sound" using the animal object
# Dog class overrides the sound() method to print: "Buddy says Woof!" using the Dog object

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

