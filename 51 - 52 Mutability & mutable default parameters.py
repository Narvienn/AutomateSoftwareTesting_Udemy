# MUTABILITY

a = []
b = a

print(id(a))
print(id(b))
# a == b - the print will return the same ID

a.append(35)
print(a)
print(b)
# same logic applies - modifying 'a' will modify 'b'
# a = [] & b = [] will create two different variables with different IDs

# Everything in Python is mutable - unless it's not ;D
# IMMUTABLE: tuples, integers, strings, floats and booleans


# e.g.

c = 1234
d = 1234

print(id(c))
print(id(d))
# This will print the same ID - the integer value for 'c' is already created so 'd' will just use it
# BUT:

c = 1234
d = 1235
# This will now change the ID of 'd' and 'c' will stay the same!


# MUTABLE DEFAULT PARAMETERS

from typing import List


class Student:
    def __init__(self, name: str, grades: List[int] = []):  # Don't do data type hinting like the last bit. More on that below.
        self.name = name
        self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)


alice = Student("Alice")
alice.take_exam(90)
print(alice.grades)

# When you create another Student object:
bob = Student("Bob")
print(bob.grades)

# This will return [90], even though take_exam was not called on bob
# That's because the default parameters are defined when the function is created, not when it's called
# What happens is, once we call take_exam for the first time with alice, it will assign 90 to grades
# ... and since lists are immutable, the parameter will stay that way

# A way out of that is passing grades (a list) when creating a Student object:

charlie = Student("Charlie", [55, 80])
# The 'default' 90 will stay the same for each Student object without its own grades parameter passed

# How best to fix it?
class Student_:
    def __init__(self, name: str, grades: List[int] = None):
        self.name = name
        self.grades = grades or []