'''Write a Python program to get the difference between a given number and 17,
if the number is greater than 17 return double the absolute difference.'''

def diff(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2


if __name__ == "__main__":
    n = int(input("enter the n value:"))
    print(diff(n))