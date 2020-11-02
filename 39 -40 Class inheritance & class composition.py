# CLASS INHERITANCE

#TODO: @classmethod & @staticmethod exercises


class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True   # if this is true, there's no need to specify *how* it's connected (the connected_by)

    def __str__(self):
        return f"Device {self.name} ({self.connected_by})"

    def disconnected(self):
        self.connected = False
        print("Disconnected.")


printer = Device("Printer", "USB")
print(printer)
printer.disconnected()

# to create a class for a specific device, you do sth like that:


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)  # this calls the __init__ of the parent/superclass (you still need to explicitly specify the arguments, though)
        self.capacity = capacity    # value calculated before print operation - max/initial capacity
        self.remaining_pages = capacity # value calculated after print operation - current capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def printing(self, pages):
        if not self.connected:
            print("Your printer is not connected.")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages


printer_ = Printer("Laserjet", "USB", 500)
printer.printing(20)
printer.disconnected()  # you can call methods from the parent class on the subclass object :)




# CLASS COMPOSITION - using classes to build other classes - recommended & used more often than inheritance

class Bookshelf:
    def __init__(self, quantity):
        self.quantity, = quantity

    def __str__(self):
        return f"Bookshelf with {self.quantity} books"


shelf = Bookshelf(20)
print(shelf)

# when creating a derivative class - DON'T do something like this
# NOTE: It breaches the Liskov substitution principle /a square is a rectangle but not all rectangles are squares/)

class Book(Bookshelf):
    def __init__(self, name, quantity):
        super().__init__(quantity)  # this inherited attribute is not useful in a Book instance
        self.name = name

    def __str__(self):  # you are overwriting the Bookshelf __str__ method as it doesn't return what we need in a Book instance
        return f"Book {self.name}"

book = Book("Middlemarch", 120)
print(book)


# COMPOSITION - "an object is composed of other objects"

class Bookshelf_:
    def __init__(self, *books): # this will collect Book objects into a dict
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)}."


class Book_():  # no need to inherit from any other class
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}."


book = Book("Vanity Fair")
book2 = Book("Canterbury Tales")
shelf_ = Bookshelf_(book, book2)    # that's the composition: objects are collected to create another object
print(shelf_)