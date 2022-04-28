'''#  Write a Python program to construct the following pattern, using a nested for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *'''

def pattern(n):
    for i in range(n):
        for j in range(i):
            print('* ', end="")
        print('')
    for i in range(n, 0, -1):
        for j in range(i):
            print('* ', end="")
        print('')

if __name__ == "__main__":
    n = int(input("Enter the value of n:"))
    pattern(n)