#  Question 1 Ans : 
class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle

# Question 2 Ans : 
class Car(Vehicle):
    def seating_capacity(self, capacity):
        return f"Name of vehicle: {self.name_of_vehicle}, Seating capacity: {capacity}"

# Question 3 Ans :
'''
Multiple inheritance is a feature in object-oriented programming where a class can inherit
attributes and methods from more than one parent class.This allows a single class to inherit
properties from multiple classes and reuse the code from each of them.
'''
class Shape:
    def __init__(self, sides=0):
        self.sides = sides

class Color:
    def __init__(self, color=None):
        self.color = color

class Square(Shape, Color):
    def __init__(self, side_length, color):
        Shape.__init__(self, 4)
        Color.__init__(self, color)
        self.side_length = side_length

sq = Square(10, "red")
print("Number of sides:", sq.sides)
print("Color:", sq.color)
print("Side length:", sq.side_length)

# Question 4 Ans :
''' Getters and setters are methods used to access and modify the values of instance
variables in an object-oriented programming language. They provide a way to encapsulate
 the internal state of an object and control how it can be accessed and modified.
 '''
 class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
        
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        self._age = age
        
    name = property(get_name, set_name)
    age = property(get_age, set_age)

person = Person("John Doe", 30)
print(person.name) # Output: John Doe
person.name = "Jane Doe"
print(person.name) # Output: Jane Doe

# Question  5  Ans :
'''
Method overriding is a feature of object-oriented programming (OOP) that allows  a
subclass to provide a different implementation of a method that is already defined
in its superclass. In other words, a subclass can override the behavior of a method
inherited from its superclass to provide its own specific implementation.
'''
class Animal:
    def make_sound(self):
        print("The animal makes a sound.")
        
class Dog(Animal):
    def make_sound(self):
        print("The dog barks.")
        
dog = Dog()
dog.make_sound() # Output: The dog barks.
