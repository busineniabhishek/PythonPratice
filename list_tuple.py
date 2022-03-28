0'''Write a Python program which accepts a sequence of comma-separated numbers from user and
generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')'''


def list_tuple(values):

    list = values.split(",")
    tup = tuple(list)
    print("the list for the given values is:",list)
    print("the tuple for the given values is:", tup)

if __name__ == "__main__":
    values = input("enter the values with commas:")
    list_tuple(values)