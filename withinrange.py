'''Write a Python program to test whether a number is within 100 of 1000 or 2000'''


def withinrange(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))


if __name__ == "__main__":
    n = int(input("enter the value of n:"))
    print(withinrange(n))
