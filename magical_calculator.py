import re

print("magical calculator")

previous = 0
run = True

def performMath():
    equation = input("Enter the equation:")
    print("you typed", equation)

while run:
    performMath()