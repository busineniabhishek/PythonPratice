"""# Write a Python program to check the validity of a password (input from users).
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
# Input
# W3r@100a
# Output
# Valid password"""

import re

class Password:

    def password_validation(self,pwd):
        x = True
        while x:
            if (len(pwd) < 6 or len(pwd) > 12):
                break
            elif not re.search("[a-z]", pwd):
                break
            elif not re.search("[0-9]", pwd):
                break
            elif not re.search("[A-Z]", pwd):
                break
            elif not re.search("[$#@]", pwd):
                break
            elif re.search("\s", pwd):
                break
            else:
                print("Valid Password")
                x = False
                break
        if x:
            print("Not a Valid Password")

if __name__ == "__main__":
    pwd= input("Enter the password:")
    pswd = Password()
    pswd.password_validation(pwd)

