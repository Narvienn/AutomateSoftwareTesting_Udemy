# WHILE LOOP

number = 3
user_input = input("Would you like to play? Y/n")

if user_input == 'y':
    user_number = int(input("Guess our number: "))
    if user_number == number:
            print("You guessed right!")
    elif abs(number - user_number) == 1:
            print("You were off by one.")
    else:
            print("Wrong number, sorry.")


# 'as long as user doesn't name n as the number, enter the loop'
number = 3
user_input = input("Would you like to play? Y/n")

while user_input != 'n':
    user_number = int(input("Guess our number: "))
    if user_number == number:
            print("You guessed right!")
    elif abs(number - user_number) == 1:
            print("You were off by one.")
    else:
            print("Wrong number, sorry.")


# this creates an infinite loop as there's no mechahism to stop it/reevaluate the initial condition. Fix it:
number = 3
user_input = input("Would you like to play? Y/n")

while user_input != 'n':
    user_number = int(input("Guess our number: "))
    if user_number == number:
            print("You guessed right!")
    elif abs(number - user_number) == 1:
            print("You were off by one.")
    else:
            print("Wrong number, sorry.")
    user_input = input("Would you like to play? Y/n") # the stop mechanism


# rework to avoid declaring user_input twice & improve the break mechanism:
number = 3


while True:
    user_input = input("Would you like to play? Y/n")

    if user_input == 'n':
        break # break mechanism to exit the loop; if not met, we enter the if-statement

    user_number = int(input("Guess our number: "))
    if user_number == number:
            print("You guessed right!")
    elif abs(number - user_number) == 1:
            print("You were off by one.")
    else:
            print("Wrong number, sorry.")




# FOR LOOP

friends = ["Alice", "Bob", "Carl", "Declan"]

for friend in friends:    # friend is a variable that takes on the first value of the list
    print(f"{friend} is a friend of mine.")  # will run however many items are in the list


for friend in range(3):  # specifies the number of loop runs
    print(f"{friend} is a friend of mine.") # NOTE: It will print out item INDEXES, not item values! i.e. 0, 1, 2)


grades = [4, 4, 5, 3, 3]
total = sum(grades)
amount = len(grades)

for grade in grades:
    total += grade  # += equals "total = total + grade"

# but: you can avoid for-loop altogether (mind the time complexity!):
print (total/amount)