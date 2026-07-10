# OBJECT = A  "bundul" of related attribues (variables)  and methods (functions)
#          Ex. phone, cap, cup bokk
#          you need a class  to create many object.

# CLASS = (blueprint) used to desing the structure and layout of an object.




class Car:   # class = car
    def __init__(self, model, year, color, for_sale): # these are objects.
       self.model = model
       self.year = year
       self.color = color
       self.for_sale = for_sale



car1 = Car("mustang", 2024, "blue", False)
car2 = Car("Maruti Suzuki alto", 2009, "red", True)
car3 =Car("Honda", 1998, "grey", False)


print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)




           
        