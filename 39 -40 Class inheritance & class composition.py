# CLASS INHERITANCE

#TODO: @classmethod & @staticmethod exercises + CLASS COMPOSITION


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