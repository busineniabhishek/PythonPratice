'''Write a Python program to calculate the sum of three given numbers, if the values are
equal then return three times of their sum.'''


def sum_thrice(x,y,z):
    sum = x + y + z
    if x == y == z:
        sum = 3*x * 3
        return sum



if __name__ == "__main__":
    x = int(input("enter the value of x="))
    y = int(input("enter the value of y="))
    z = int(input("enter the value of z="))
    print(sum_thrice(x,y,z))