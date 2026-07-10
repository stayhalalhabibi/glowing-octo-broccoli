print("good evening Akshara maam AKA akka");

# The foru principal or methods are:-

# A) ENCAPSULATION = Hiding data and allowing controlled access through methods.

print("ENCAPSULATION")
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

account.deposit(500)

print(account.get_balance())  # 1500

# B) ABSTRACTION =  Hiding implementation details and showing only essential functionality.

print("B) ABSTRACTION")

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car starts with a key")


car = Car()
car.start()

# C) INHERITENCE = Creating a new class from an existing class to reuse code.

print("C) INHERITENCE")

class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()    # Inherited from Animal
dog.bark()   # Dog's own method

# D) POLYMORPHISM = Allowing the same method to perform different behaviors depending on the object.

print("D) POLYMORPHISM")

class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()