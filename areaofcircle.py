'''Write a Python program which accepts the radius of a circle from the user and compute the area.
Sample Output :
r = 1.1
Area = 3.8013271108436504
'''

def areaofcircle():
    r = float(input("enter the radius value:"))
    area = 3.141 * r*r
    print(area)

areaofcircle()