# A dictionary is a key-value pair where the key is a hashable data type (string or int)

friend_ages = {"Alice": 25, "Bob": 27, "Charlie": 30}

# getting keys - iterating by index won't work, you have to use the key:
print(friend_ages["Alice"])

# adding new pairs or modifying existing ones:
friend_ages["Declan"] = 22


# dictionary list - normally, dictionaries have multiple items, best stored in a list
friends = [
    {"name":"Alice", "age":25},
    {"name":"Bob", "age":27},
    {"name":"Charlie", "age":30}
    ]

# now you can use index to access particular k-v pairs (because this is a list of dicts):
print(friends[0]) # prints the entire dictionary (all pairs)
print(friends[0]["name"]) # prints value for selected key


# iterating over a dictionary:
student_attendance = {"Alice": 98, "Bob": 95, "Charlie": 85}

for student in student_attendance:
    print(student)  # will only print the keys!
    print(f"{student}: {student_attendance[student]}")  # prints key + value for that key

# a nicer way to do the above:
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")   # two variables in for-loop are linked to key and value, respectively


# getting just the values:
attendance = student_attendance.values()
print(sum(attendance)/len(attendance))
