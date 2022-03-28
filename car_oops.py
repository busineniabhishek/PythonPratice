class Car:

    car_type = 'sedan'

    def __init__(self,name,mileage):
        self.name = name
        self.mileage = mileage

    def description(self):
        return f"the {self.name} car gives the mileage of {self.mileage}km/l"

    def max_speed(self,speed):
        return f"the {self.name} runs at the max speed of {speed}km/hr"


Honda = Car("Honda City",21.4)
print(Honda.max_speed(150))

Skoda = Car("Skoda Octavia",13)
print(Skoda.max_speed(210))