# PACKING ARGUMENTS INTO A SINGLE TUPLE

def multiply(*args):    # this notation means: the args will be collected into a tuple once this function is called
    print(args)

multiply(1, 3, 5) # will print a tuple of (1, 3, 5)

def multiply_(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total

print(multiply_(1, 3, 5)) # will now return 15 + print because remember, return != print/show anything


def add(x, y):
    return x + y

# UNPACKING VARIABLES TO USE AS ARGUMENTS
nums = [3, 5]
add(*nums) # this will map the 1st arg to x and 2nd arg to y = destructuring the nums variable
# otherwise:

add(nums) # this will cause nums to be passed to x and nothing to be passed to y => TypeError (missing positional arg)

# UNPACKING DICTIONARIES
numbers = {'a': 15, 'b': 20}
print(add(**numbers))   # The ** means "unpack all values onto the function parameters sequentially"


def apply(*args, operator): # This means: collect all args into a tuple + have an obligatory named argument at the end
    if operator == "*":
        return multiply(*args) # need to unpack the tuple first so that it's not passed in whole (see function definition)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."

print(apply(1, 3, 5, operator='+')) # If you miss the 'operator=' syntax, Python will collect it with the other args (+ throw an error)