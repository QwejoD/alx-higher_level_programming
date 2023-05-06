#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it to stdout"""


"""Define a text file-reading function."""
def read_file(filename=""):

    """Print the content of a UTF8 to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
