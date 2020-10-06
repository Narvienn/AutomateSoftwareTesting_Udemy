15-18 Booleans and IF statements


# BOOLEANS - watch out:

friends = ["Alice", "Bob"]
friends_abroad = ["Alice", "Bob"]

print(friends == friends_abroad) # returns TRUE - same value assigned to both variables
print(friends is friends_abroad)  # returns FALSE  - same value but different memory cells!


# IF statements with IN keyword

besties = ["Charlie", "Declan", "Emma"]
print("Emma" in besties)    # IN keyword makes this print expression a logic test for a Boolean value - returns TRUE

someones_bestie = input("And who's your bestie?").lower  # .lower() unifies spelling of user input / eliminates uppercase vs lowercase

if someones_bestie in besties:
    print(f"{someones_bestie} is my best friend too!")
else:
    print("We can't all like the same people, right?")