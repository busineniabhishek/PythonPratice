'''Write a Python program to get the volume of a sphere with radius 6'''

def volume(r):

    volume = 4.0/3.0 * 3.14* r**3
    print(volume)

if __name__ == "__main__":
    r  = int(input("enter the r value:"))
    volume(r)