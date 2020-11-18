# FIRST CLASS FUNCTION is a function that you can use as an argument in a different function
# here - divide is the first-class function:
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("You can't divide by 0!")
    return dividend/divisor


def calculate(*values, operator):
    return operator(*values)    # duck typing (?) - 'operator()' variable has the syntax of a function therefore it's interpreted as a function


result = calculate(20, 4, operator=divide)  # divide function value is passed as an operator argument here
print(result)
# HOW? 20 and 4 are collected as (20, 4) because of the *values syntax and assigned as dividend and divisor, respectively, in divide
# NOTE: the divide function is not called here just yet, only used as an argument - if you wanted to call it, the syntax would have to be 'operator=divide())


# Example 2
def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")


friends  = [
    {"name": "Anne Smith", "age": 24},
    {"name": "Bob Jones", "age": 25},
    {"name": "Carl Davies", "age": 26}
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends), "Bob Smith", get_friend_name)
# in this function call: friends == sequence, what we will iterate over; "Bob Smith" == expected, get_friend_name == finder

# NOTE: You can use lambda instead:
print(search(friends, "Alice Davies", lambda: friend["name"]))

