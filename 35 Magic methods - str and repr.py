# Methods with two preceding and trailing underscores are called 'magic' methods, e.g. like __init__

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Calling Person() is the same as Person.__init__

Alice = Person("Alice", 25)
print(Alice)

# Printing an object prints its system address: <__main__.Person object at 0x000001FFCDA53E80>
# You can only print a string - and an object isn't one
# This is fixed with __str__ and __repr__ methods:

class Person_:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # converts the object to a printable string
        return f"Person: {self.name}, age: {self.age} years old."


    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"
    # The acute brackets are to show to programmers that this is a 'pretty printout' of an object - an unambiguous representation
    # It's used chiefly e.g. in debugging


# print(Alice) now returns the string from __str__