

numbers  = [1,3,5,8]
doubled = []

for number in numbers:
    doubled.append(number * 2)

# Too many lines - compress it like so:

nums  = [1,3,5,8]
doubled = [x * 2 for x in nums] # i.e. do this for each item in list (that meets critera x, y, z)

# example 2
friends = ['Alice', 'Bob', 'Carl', 'Declan', 'Daria']
starts_d = []

for friend in friends:
    if friend.startswith("D"):
        starts_d.append(friend)


# a cleaner, more concise version:
folks = ['Alice', 'Bob', 'Carl', 'Declan', 'Daria']
starts_with_d = [friend for friend in folks if friend.startswith("D")]


