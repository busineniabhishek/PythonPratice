'''rite a Python program which accepts the user's first and last name and print them in reverse
order with a space between them.'''

def wordrev(first_name,second_name):

    str1 = second_name + " " + first_name
    print(str1)


if __name__ == "__main__":
    first_name = input("enter the firstname:")
    second_name = input("enter the secondname:")
    wordrev(first_name,second_name)