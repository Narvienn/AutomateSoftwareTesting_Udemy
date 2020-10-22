def named(**kwargs):    # 'kwargs' isn't a keyword - you can name these arguments whatever you like
    print(kwargs)


named(name="Alice", age=25)
# This will print a dictionary: {'name': 'Alice', 'age': 25
# That dictionary will then become a single argument - that's what the ** in function def does!


def named_(name, age):
    print(name, age)

details = {"name": "Bob", "age": 25}

named(details) # This won't work: details is a dict of 2 items - you can't pass it as a single positional argument for the name parameter in function def
# Thus, the name parameter has details as value while age parameter has none

# To pass "name" key as value for name parameter and "age" value as value for age parameter, do this:

named(**details) # This will now return "Bob" and "25"

def print_nicely(**kwargs):     # ** will pack the keyword arguments into a dictionary
    named(**kwargs)             # will print that dictionary
    for arg, value in kwargs.items():       # creates arg and value variables and items() iterates over the dictionary
        print(f"{arg}: {value}")


print_nicely(name="Bob", age=25)


# USING BOTH TYPES OF (UN)PACKING

def both(*args, **kwargs):  # will collect all positional args into a tuple and all named arguments into a dictionary
    print(args)
    print(kwargs)


both(1, 3, 5, name="Bob", age=25) # will print a tuple of (1, 3, 5) and a dict of {"Bob": 25}

# This is often done in functions that call other functions, e.g.:
def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)