class TooManyPagesReadError(ValueError):    # custom errors/exceptions needs to inherit from Python built-in errors/exceptions
    pass    # in this case, ValueError class already has a method for what we need
# traceback message will return both the error and the error message


class Book:
    def __init__(self, name: str, page_count: int): # data typing
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f"<Book {self.name} with {self.page_count} pages"
        )

    def read(self, pages: int):
        # custom error class - needs to be defined in a class of its own before it's used in a function
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.pages_read + pages} pages but the book only has {self.page_count} pages."
            )
        self.pages_read += pages
        print(f"You have read {self.pages_read} out of {self.page_count}")


python101 = Book("Python 101", 50)
python101.read(35)
python101.read(80) # this will naturally return "You have read 80 out of 50 pages" - to prevent that, we need a custom error class


# instead, after creating your custom error, do this:

try:
    python101.read(60)
except TooManyPagesReadError as e:  # e is the variable for the contents of the error
    print(e)    # will only print the error message and not the entire traceback
