'''Write a Python program to construct the following pattern, using a nested loop number'''

def num_pattern(upper_limit,lower_limit):

    num = lower_limit
    while num < upper_limit:
        num_1 = str(num) * num
        print(num_1)
        num = num + 1

if __name__ == "__main__":
    lower_limit = int(input("Enter the lower limit: "))
    upper_limit = int(input("Enter the upper_limit:"))
    num_pattern(upper_limit,lower_limit)