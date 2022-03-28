'''Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
Sample filename : abc.java
Output : java'''


def filetype(filex):

    str = filex.split(".")
    print("the extension of the given file is:",str[-1])


if __name__ == "__main__":
    filex = input("enter the file type:")
    filetype(filex)