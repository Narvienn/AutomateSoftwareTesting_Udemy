# DEFAULT PARAMETER VALUES

def add(x,y=8):    # x is a required parameter, y will be equal to 8 unless a different argument value is passed in call)
    print(x + y)

add(5) # 5 is interpreted as value of x, and since y is predefined/default = 8, there's no need to pass it in the call)
add(x=5) # will do the same as above
# as usual, positional argument precedes a keyword one

# NOTE: don't do something like that:

default_y = 3

def add_(x, y=default_y):
    sum = x + y
    print(sum)

# Why? Because the default value is defined only once - changing the global variable outside function will not affect the default parameter!


# FUNCTION RETURNING VALUES

add(5, y=9)
result = add(5, y =9)
print(result)

# the last line will return None instead of 14
# Why? Because by default, functions return nothing - that's why you need to explicitly state what it should return:

def addition(x, y):
    return x + y

# NOTE: Return != print
# NOTE2: Return terminates the function

def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You broke the universe!"        # only one return will run in this function so this is fine

# NOTE: functions should not normally return different data types


result = divide(15, 3)
print(result)

