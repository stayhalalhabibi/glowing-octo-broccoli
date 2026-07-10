# INHERITENCE  = ALlows a class to inherit attributes and methods from another class 

#              helps with code reusability adn extensibilty class child (parent).

#              Tight Coupling,Increased Complexity,Reduced Flexibility,Changes Can Cause Problems





# Parent Class
class Animal:
    def sound(self):
        print("Animals make sounds")

# Child Class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Create object
d = Dog()

# Access parent class method
d.sound()

# Access child class method
d.bark()