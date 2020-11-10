def divide(dividend, divisor):
    # if divisor == 0:
    #     print("You cannot divide by 0.")
    #     return
    return dividend/divisor

divide(15, 0)

grades = []
print("Welcome to the grade average program.")
if len(grades) == 0:
    print("You don't have any grades yet.")     # This provision takes the function logic out of function def - not the best idea!
average = divide(sum(grades), len(grades))
print(f"Your average is {average}")


# Raise error/exception instead:
# Errors/exceptions are in-built Python classes (see docs for more info!)

def divide_(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

# When predicting that an error could occur, it's best to prepare your program for it with try/except:
grades_ = []
try:
    average_ = divide(sum(grades_), len(grades_))   # the code we want to run normally
    print(f"Your average is {average}")
except ZeroDivisionError:   # the exception that can predictably happen
    print("You don't have any grades yet.")


# NOTE: try/except only applies locally - using the divide function elsewhere with divisor=0 will not print the 'except' message
# It will print the message from the function, which is global


# NOTE: You can also have code that only runs if the error in try/except was not raised:
grade_list = []
try:
    avg = divide(sum(grades_), len(grades_))
except ZeroDivisionError:
    print("You don't have any grades yet.")
else:
    print(f"Your average is {avg}") # is only executed if except clause didn't run
finally:
    print("Thank you")  # will only run after the try, (except), and else clauses are run


# Example:

students: [
    {"name": "Alice", "grades": [80, 87]},
    {"name": "Bob", "grades": []},
    {"name": "Charlie", "grades": [90, 97]}
]
try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average_grade = divide(sum(grades), len(grades))
        print(f"{name}'s average is {average_grade}")
except ZeroDivisionError:
    print(f"ERROR: {name} has no grades.")
else:
    print("All student grades have been calculated.")
finally:
    print("End of calculation.")




