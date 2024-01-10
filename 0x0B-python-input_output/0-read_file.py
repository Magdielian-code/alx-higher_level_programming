#!/usr/bin/python3
"""This module defines a text file-reading function"""

def read_file(filename="", text=""):
    """Prints the contents of the text file"""
    with open(filename,"w", encoding="utf-8") as f:
        print(f.read(), end="")
