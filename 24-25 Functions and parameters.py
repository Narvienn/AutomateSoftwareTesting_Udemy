# DEFINING AND CALLING A FUNCTION

def user_age_in_hours():    # function definition
    user_age = int(input("Enter your age"))
    age_hours = user_age * 365 * 24
    print(f"Your age in hours is {age_hours}")

# function call, e.g.
print("Wanna know how old you are in hours?")
user_age_in_hours()
print("And now you know!")

# NOTE: there's a difference between a 'global' variable and an in-function variable, cf.

friends = ["Alice", "Bob"]

# note: using the same variable inside a function and outside of it creates TWO variables (different memory cells):

friends = ["Alice", "Bob"]
extended_friends = []
def add_friend():
    friend_name = input("Enter a friend's name:")
    friends = extended_friends.append(friend_name) # in-function variable 'friends' shadows same-named global variable - DON'T DO THAT


# POSITIONAL ARGUMENTS

def add(x, y):  # parameters are defined right here (if they aren't defined elsewhere)
    pass # Python for 'do nothing' - placeholder as indented block of code is required after a def statement

# when calling a function and providing values for parameters, parameters become arguments
add(5, 3)
# 5  becomes x, 3 becomes y - POSITIONAL ARGUMENTS


def add_args(x, y):
    result = x + y
    print(result)


# DEFINING PARAMETERS:
def say_hello(name):
    print(f"Hello there, {name}")


say_hello("Alice")  # "Alice" is then assigned to the name parameter and becomes a positional argument


# NAMED/KEYWORD ARGUMENTS

def introduction(name, surname):
    print(f"Hello, {name} {surname}")


introduction(name='Alice', surname='Smith')


def division(dividend, divisor):
    if divisor != 0:
        print(dividend/divisor)
    else:
        print("Great, you just exploded the universe!")


# you can call the function with both keyword/named arguments:
division(dividend=15, divisor=3)

# ... or with only one keyword argument - but the positional argument has to come first:
division(15, divisor=5)
