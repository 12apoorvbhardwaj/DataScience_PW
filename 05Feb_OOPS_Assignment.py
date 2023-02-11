# Question 1 Ans :

'''
In object-oriented programming, a class is a blueprint or a template for creating objects. It defines a set of attributes
and methods that the objects created from the class will have. A class is like a blueprint of a real-world entity, such as a car or a person.

An object, on the other hand, is an instance of a class. It is a specific occurrence of a class, and it has its own state and behavior.
An object can be thought of as a real-world entity, such as a specific car or a specific person.

Here's an example to illustrate the concept of classes and objects:
'''
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start(self):
        print("Starting the car")
    
    def stop(self):
        print("Stopping the car")

my_car = Car("Toyota", "Camry", 2022)
print(my_car.make)
print(my_car.model)
print(my_car.year)
my_car.start()
my_car.stop()

your_car = Car("Honda", "Civic", 2020)
print(your_car.make)
print(your_car.model)
print(your_car.year)
your_car.start()
your_car.stop()


# Question 2 Ans :
'''
Abstraction: Hiding the implementation details and exposing only the necessary information to the outside world.

Encapsulation: Wrapping data and functions within an object to protect it from outside interference and misuse.

Inheritance: Creating a new class based on an existing class, inheriting its properties and behaviors.

Polymorphism: The ability of objects of different classes to respond to the same method call, each one in its own way.
'''

# Question 3 Ans :

'''The __init__ method, also known as the constructor method, is used to initialize the attributes of an object when it is created.
This method is automatically called when an object is created from a class and it is the first method that is executed.


The self argument is a reference to the instance of the object being created, and it is automatically passed to the method when the
object is created. The other arguments are the attributes that you want to initialize for the object.
'''
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog = Dog("Rufus", "Labrador")
print(dog.name)
print(dog.breed)


# Question 4 Ans :
'''
self is a reference to the instance of the object that is calling the method. It is used to access the attributes and methods of the object.
In Python, every method in a class must have self as its first parameter. When you call a method on an object, the object is automatically 
passed as the first argument to the method, and the reference to the object is stored in the self variable. This allows you to access the attributes and methods of the object within the method. 
'''
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof! My name is", self.name)

dog = Dog("Rufus", "Labrador")
dog.bark()


# Question  5 Ans :
# Inheritance :

# Single Inheritance:

#  In single inheritance, a derived class inherits from a single base class. 
# This is the most basic form of inheritance. Here's an example:
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def __init__(self, breed):
        Animal.__init__(self, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Woof!")

dog = Dog("Labrador")
dog.make_sound()

# Multi-level Inheritance:
 
# In multi-level inheritance, a derived class inherits from a base class, which in turn inherits from another base class.
# This allows the derived class to inherit attributes and methods from multiple levels of base classes. Here's an example:
class Grandparent:
    def __init__(self, name):
        self.name = name

class Parent(Grandparent):
    def __init__(self, name, occupation):
        Grandparent.__init__(self, name)
        self.occupation = occupation

class Child(Parent):
    def __init__(self, name, school):
        Parent.__init__(self, name, occupation="Teacher")
        self.school = school

child = Child("Alice", "Elementary School")
print(child.name)
print(child.occupation)
print(child.school)

#Multiple Inheritance:

#In multiple inheritance, a derived class inherits from multiple base classes. This allows the derived class to inherit attributes
# and methods from multiple base classes. Here's an example:
class Mother:
    def __init__(self, name, eye_color):
        self.name = name
        self.eye_color = eye_color

class Father:
    def __init__(self, name, hair_color):
        self.name = name
        self.hair_color = hair_color

class Child(Mother, Father):
    def __init__(self, name, school):
        Mother.__init__(self, name, eye_color="Brown")
        
