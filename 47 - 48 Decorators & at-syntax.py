
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