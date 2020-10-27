# INSTANCE METHOD - any method that uses class object ( = instance)  as first parameter (self)

class ClassTest:
    # NOTE: __init__ isn't required if there's no initialization needed for the class - but 'self' is still needed
    def instance_method(self):  # only runs on an instance/object of the class
        print(f"Just called instance method for {self}")

# Calling instance methods - version 1:
test = ClassTest()
test.instance_method()
# Version 2:
ClassTest.instance_method(test)
# Both will print: "Just called instance method for <__main__.ClassTest object at 0x000001E07B935438>"


# CLASS METHOD

class Class_Test:
    def instance_method(self):
        pass

    @classmethod
    def class_method(cls):  # the cls parameter is a class itself
        print(f"Just called class_method of {cls}")
    # Class methods are used as factories

    @staticmethod
    def static_method():    # no default or implicit parameter - this function is independent of either instance or class
        print("Called static_method.")
    # Static methods are used when it makes sense to group a function within a class but there's nothing to explicitly tie it with either instance or class

# Calling a class method:
Class_Test.class_method()   # no need to pass a parameter - 'Class_Test' is implicitly passed
# Will print: "Just called class_method of <class '__main__.Class_Test'>"


# Example of a class method used as a factory:

class Book:
    TYPES = ("hardcover", "paperback")  # in-class variables become class properies

    def __init__(self, name, book_type, page_count):
        self.name = name
        self.book_type = book_type
        self.page_count = page_count

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, numbering {self.page_count} pages>"

    # Note: so far, there was no check/use for TYPES. Here's how to change that - create a factory:
    @classmethod
    def hardcover(cls, name, page_count):
        return Book(name, Book.TYPES[0], page_count) # Voila - you created a new class object/instance inside that class!
    # NOTE: the above could/should be written like so: return cls(name, cls.TYPES[0], page_count) - because cls and Book are interchangeable here


volume = Book("Moby Dick", "hardcover", 500)
print(volume)   # thanks to the __repr__ method, this can be done now

book = Book.hardcover("Middlemarch", 450)   # no need to pass type as it's defined in the class method we just called





