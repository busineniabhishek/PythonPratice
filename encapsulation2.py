class Car:

    def __init__(self,name,mileage):
        self.__name = name
        self.mileage = mileage

    def description(self):
        return f"The {self.__name} car gives the mileage of {self.mileage}"


obj = Car("BMW 7-series",39.53)

#accessing private variable via class method
print(obj.description())

#accessing private variable directly from outside
print(obj.mileage)
print(obj._Car__name)      #mangled name