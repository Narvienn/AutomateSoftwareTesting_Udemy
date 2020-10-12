
x = 5, 11 # brackets welcome but not required - Python will interpret is as x = (5, 11), a tuple

z, y = 6, 12 # equals z = 6 and y = 12


student_attendance = {"Alice": 98, "Bob": 95, "Charlie": 85}

print(list(student_attendance.items())) # changes the dictionary to a list of tuples

for t in student_attendance.items():
    print(t)

# will return this:
# ('Alice', 98)
# ('Bob', 95)
# ('Charlie', 85)
# It prints every list item, and the list() method changed dict items into tuples
# And the tuple? Can be destructured:

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

    # this is why this notation works

people = [('Alice', 42, 'teacher'), ('Bob', 43, 'mechanic'), ('Charlie', 41, 'writer')]
for name, age, profession in people:        # will desctructure the tuple into three separate items
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

# without desctructuring, this loop could look like this:

for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")


# How to ignore a variable when destructuring a list/tuple? Underscore it:
# person = name, _, profession
# print(name, profession)

#Destructuring with HEAD and TAIL:

head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)

# Will result in 1 and [2,3,4,5]. Similarly:

*head, tail = [2,3,4,5]

# Will result in [2,3,4] and 5
