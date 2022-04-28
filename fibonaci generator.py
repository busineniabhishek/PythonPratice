'''Write a Python program to get the Fibonacci series between 0 to 50'''

def fibonaci(limit):
    x, y = 0, 1
    while y < 50:
        print(y)
        x, y = y, x + y


if __name__ == "__main__":
    limit = int(input("Enter the lower limit:"))
    fibonaci(limit)