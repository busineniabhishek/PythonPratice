'''How to inherit a parent class? Use the following syntax:'''
# class parent_class:
#     body of parent class
#
# class child_class( parent_class):
#     body of child class

class Car:

    def __init__(self,name,mileage):
        self.name = name
        self.mileage = mileage

    def description(self):
        return f"The {self.name} car gives the mileage of {self.mileage}km/l"

class BMW(Car):
    pass

class Audi(Car):
    def audi_desc(self):
        return "This is the description of the audi"

obj1 = BMW("BMW 7-series",39.53)
print(obj1.description())

obj2 = Audi("Audi A8 L",14)
print(obj2.description())
print(obj2.audi_desc())