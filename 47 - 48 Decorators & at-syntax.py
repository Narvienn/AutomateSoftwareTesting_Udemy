
user = {"username": "Bill", "access_level": "admin"}


def get_admin_pword():
    return "1234"

print(get_admin_pword())

# Step 1: to protect admin password, the first that comes to mind is an if-statement:
if user["access_level": "admin"]:
    print(get_admin_pword())

# BUT! The if-statement only secures this one occurrence of that function call - you can still call it again, which will be unprotected

# Step 2: define a secure admin password getting method:
def secure_get_admin_pword():
    if user["access_level": "admin"]:
        print(get_admin_pword())
    return "1234"

# Step 3 - instead of deleting the original unsecure get_admin_pword, we can do this:

def secure_function(func):  # passing a first-class function as function parameter
    if user["access_level"] == "admin":
        return func


get_admin_password = secure_function(get_admin_pword)
print(get_admin_pword())




# @-syntax in decorators - instead of the latter notation (i.e. pass get_admin_pword as argument in secure_function, you can do this:

def make_secure(func):
    def secure_function_():
        if user ["access_level"] == "admin":
            return func()
        else:
            return f"No admin permission for {user['username']}"
    return secure_function_

@make_secure    #This will make the function below be created + passed as argument through the function defined in make_secure
def get_admin_pword_():
    return "1234"

# NOTE: Decorator can only be defined once: if you change the function under the decorator, the decorator will still refer to the original func

print(get_admin_pword.__name__) # will still print secure_function, even if the function itself was deleted

# How to fix this? Import functools and use them as decorator in your decorator, like so:

import functools

def make_secure_(func):
    @functools.wraps(func)  # NOTE: put the wrapper INSIDE the decorator function, not on top of it
    def secure_functionB():
        if user ["access_level"] == "admin":
            return func()
        else:
            return f"No admin permission for {user['username']}"
    return secure_functionB
