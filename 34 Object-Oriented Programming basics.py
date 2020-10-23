student = {'name': 'Rolf', 'grades': (90, 89, 88, 91)}

def average(sequence):
    return sum(sequence) / len(sequence)

print(average(student['grades']))
# That's technically correct but the point of OOP is to be able to do sth like this:

print(student.average())    # calling this function is not allowed on a dictionary, so...

class Student:  # defining a class so that later we can create objects based on it
    def __init__(self): # constructor function defines basic qualities of the class
        self.name = 'Rolf'
        self.grades = (90, 89, 88, 91)

    def average(self):  # all class methods need the 'self' parameter - to pass the object to it
        return sum(self.grades) / len(self.grades)



student = Student() # when creating an object of a class, it will automatically call the init method
# any properties in the init are assigned to an empty object, which is then assigned to the variable
# and it's now possible to refer to that property:
print(student.name)
print(student.grades)

# Now we can call the average method like so:
print(Student.average(student))

# but it's better to do it on the object, not the class:
print(student.average())


# NOTE: __init__ can take more arguments than self:
class Pupil:
    def __init__(self, name):
        self.name = name    # this parameter will take the value of the argument passed in name (e.g. Bob, like below)

pupil = Pupil('Bob')
print(pupil.name)   # will now print 'Bob' because that's what was passed to __init__
