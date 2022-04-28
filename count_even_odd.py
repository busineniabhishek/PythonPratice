'''# Count the number of even and odd numbers from a series of numbers
# Input
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
# Output
# Number of even numbers : 4
# Number of odd numbers : 5 '''

def evenodd_count(u_limit,l_limit):
    e = o = 0
    for i in range(l_limit,u_limit+1):
        if i % 2 == 0:
            e = e + 1
        else:
            o = o + 1
    print("count of even num:",e)
    print("count of odd num",o)


if __name__ == "__main__":
    u_limit = int(input("Enter the upper limit:"))
    l_limit = int(input("Enter the lower limit:"))
    evenodd_count(u_limit, l_limit)