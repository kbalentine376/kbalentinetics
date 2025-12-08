import time

characterName = input("Welcome to my tavern young traveler, what is your name? ").capitalize()
print()

while True:
    tavernQuest = input(characterName + ", I have a quest for you, are you interested? Yes/No: ").capitalize()
    if tavernQuest == "Yes":
        print("I need a dragons scale for something I am testing.")
        time.sleep(2)
        print("There is a cave nearby where a dragon resides, I'll pay you once I have the scale.")
        time.sleep(3)
        print("Here is a map to the cave.")
        print() 
        break

    elif tavernQuest == "No":
        print("I will not allow you to leave without resources, you must accept my quest, let me ask again.")
        print() 

    else:
        print("Sorry, I didn't catch that. Could you repeat that?")
        print() 

time.sleep(2)
print("You begin your adventure for the scale by first leaving the tavern. Once outside you take a look at the map, it's torn and beaten.")
print("Looking at the map you notice the cave is down a path to the left of your current location, you begin heading that way.")
print()

time.sleep(8)
print("You stop at a fork in the path, two trails. You look at your map and notice they both lead to the cave.")
print("The path to the left is shorter than that to the right. You may also decide to leave.")
print()

time.sleep(7)
while True:
    fork = input("Which option do you choose? Left/Right/Leave: ").capitalize()
    if fork == "Left":
        print("You have chosen the path to the left.")
        time.sleep(2)
        print("By going down the trail to the left you save close to a day of walking.")
        time.sleep(3)
        print("The cave now visible where you stand you notice the dragon in its cave.")
        time.sleep(3)
        print("Too late to turn back you must move on, you must get the scale.")
        break

    elif fork == "Right":
        print("You have chosen the path to the right.")
        time.sleep(2)
        print("Taking longer than the shorter path you are slim on resources, no mistakes can be made.")
        time.sleep(3)
        print("In the distance you are able to see the dragons cave, its empty, a scale laying on the nest.")
        break

    elif fork == "Leave":
        print("You have decided to leave and head back to the town.")
        time.sleep(2)
        print("You return empty handed.")
        print()
        break

    else:
        print("You have confused yourself in your own thoughts.... Lets try that again.")
        print()
        time.sleep(2)

time.sleep(3)
if fork == "Left":
    while True:
        left = input("") 

if fork == "Right":
    while True:
        print()

if fork == "Leave":
    print("You have lost, with no pay you have nothing to buy")