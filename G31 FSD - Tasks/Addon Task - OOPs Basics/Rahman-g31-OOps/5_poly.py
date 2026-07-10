#  POLYMORPHISM = (MANY FORMS)
                 # It allows the same method or function to perform different actions depending on the object.
                 #Example: A person behaves differently as a student, teacher, or parent, even though they are the same person.

# Compile-Time Polymorphism

#Compile-time polymorphism is achieved by method overloading, where multiple methods have the same name but different parameters.

class Calculator:
    def add(self, a, b=0):
        return a + b

c = Calculator()

print(c.add(5))
print(c.add(5, 10))


#  Runtime Polymorphism
#                    Runtime polymorphism is achieved by method overriding, where the child class provides its own implementation of a method inherited from the parent class.

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.sound()
c.sound()