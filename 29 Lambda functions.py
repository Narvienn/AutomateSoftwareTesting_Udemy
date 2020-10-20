# LAMBDA is a short (usually nameless) function that does a single calculation of its inputs and returns a single output


def add(a, b):
    return a + b

print(add(5, 7))

# could be replaced with:

lambda x, y: x + y # no need to explicitly state return, that's what the after-colon statement does

# lambda can still have a name - when you assign it to a variable:

add = lambda x, y: x + y
print(add)

# you can define AND call a lambda on arguments like so:
(lambda x, y: x + y)(5, 7) #... but it's not very common, or useful


def double(x):
    return x * 2

sequence = [1, 3, 5, 8, 13]
doubled = [double(x) for x in sequence]


# MAP function

doubled_ = map(double, sequence) # 'run the function on the variable/its items'
# this is common in other programming languages, which don't usually have list comprehensions

# using a lambda, the above will loke like this:
doubled_2 = list(map((lambda x: x *2), sequence)) # map function doesn't return a list by default - it returns a map object