users = [
    (0, "Alice", "password"),
    (0, "Bob", "passw0rd"),
    (0, "Charlie", "admin1"),
    (0, "Declan", "asdfdshg"),
    ]


username_mapping = {user[1]: user for user in users} # (key: value)
# this takes the username and assigns to it the entire user tuple - it makes the username into the key

# this way, querying by username gets you the whole user record:
print(username_mapping["Alice"])

# without mapping/dictionary comprehension, you would have to do it like so:
for user in users:
    if user[1] == "Alice":
        print(user)


