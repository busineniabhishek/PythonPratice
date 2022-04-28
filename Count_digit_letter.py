'''# Write a Python program that accepts a string and calculate the number of digits and letters
# Sample Data : "Python 3.2"
# Expected Output :
# Letters 6
# Digits 2'''

def digit_num(str):
    d = l = 0
    for c in str:
        if c.isdigit():
            d = d+1
        elif c.isalpha():
            l = l+1
        else:
            pass
    print("count of letters:",l)
    print("count of digits:",d)


if __name__ == "__main__":
    str = input("enter the string: ")
    digit_num(str)


