# Two methods for imports:

# METHOD 1 - imports specific functionalities:
from unittest import TestCase
TestCase()

# METHOD 2 - imports the entire module and you call its functionalities as you need them:
import unittest
unittest.TestCase()


# Built-in Python module handling imports:
import sys
print(sys.path) # prints a list of paths to folders where importable packages are stored

# NOTE: when creating a folder with importable files/modules, it's a good practice to create an __init__ .py file in that folder



# RELATIVE IMPORTS
# if you have a module folder and files in it, you can do e.g. from libs.operations import operator
# the syntax: .mymodule means "current folder"

