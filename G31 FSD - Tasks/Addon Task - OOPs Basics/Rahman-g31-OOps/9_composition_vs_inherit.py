
#  What is the Difference Between Composition and Inheritance.

# INHERITENCE = an object-oriented programming concept where a child class inherits the properties and methods of a parent class. 
# It represents an "is-a" relationship. For example, a Dog is an Animal, so the Dog class can inherit from the Animal class.

# COMPOSITION = a concept where one class contains an object of another class to reuse its functionality. It represents 
# a "has-a" relationship. For example, a Car has an Engine, so the Car class contains an Engine object instead of inheriting from it.


# INHERITENCE

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()
d.bark()

# COMPOSITION

class Engine:
    def start(self):
        print("Engine Started")

class Car:
    def __init__(self):
        self.engine = Engine()   # Composition

    def drive(self):
        self.engine.start()
        print("Car is moving")

c = Car()
c.drive()