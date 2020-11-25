import functools

user = {"username": "Bill", "access_level": "admin"}


def make_secure(func):
    @functools.wraps(func)  # NOTE: put the wrapper INSIDE the decorator function, not on top of it
    def secure_functionB(panel):
        if user ["access_level"] == "admin":
            return func(panel)
        else:
            return f"No admin permission for {user['username']}"
    return secure_functionB

@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "secure_password"


print(get_password("billing")) # This won't work: the decorator returns func() without the argument
# When you run get_password, secure_functionB is called (as per @make_secure decorator, and secure_functionB does not take an argument

# (Tentative) solution: make the secure_function pass the panel argument (see above)
# BUT: This couples secure_functionB with get_password, making it unusable for other operations!

# Actual solution: passing collected arguments:

def make_secure_param(func):
    @functools.wraps(func)  # NOTE: put the wrapper INSIDE the decorator function, not on top of it
    def secure_functionC(*args, **kwargs):
        if user ["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permission for {user['username']}"
    return secure_functionC


# DECORATORS WITH PARAMETERS

# If you want to limit the running of each function based on user rights - wrap your decorator with another decorator, with the parameter you need:

def decoratoresque_function(access_level):  # By doing so, the wrapping function becomes a factory of decorators and make_secure_param is decorator proper
    def make_secure_param(func):
        @functools.wraps(func)  # NOTE: put the wrapper INSIDE the decorator function, not on top of it
        def secure_functionC(*args, **kwargs):
            if user ["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permission for {user['username']}"
        return secure_functionC
    return decoratoresque_function


@make_secure_param("admin") # The brackets are needed now that the function takes parameters
def get_admin_pword():
    return "Admin: 1234"


@make_secure_param("user")
def get_dash_pword():
    return "user: user_pword"

