# HANDLING USER INPUT


flat_size_sqft = input("How big is your flat (in square feet)?")
sq_ft = int(flat_size_sqft) # by default, user input is a string
sq_m = round((sq_ft / 10.8), 2)
print(f"{sq_ft} square feet is ca. {sq_m} square metres.")



# STRING FORMATTING

name = "Alice"
greeting = f"Hello, {name}"

print(greeting)

# This requires declaring the name variable each time we need to use a different one.
# Better option -- a template:
first_name = "Bob"
greeting2 = "Hi, {}"
greeting_with_name = greeting2.format(first_name)

print(greeting_with_name)

# templates can be reused:
greeting_with_name2 = greeting2.format("Carl")
print(greeting_with_name2)

# You can insert multiple arguments into strings:
phrase = "Hello, {}. The time is {}."
completed_phrase = phrase.format("Declan", "4 pm")