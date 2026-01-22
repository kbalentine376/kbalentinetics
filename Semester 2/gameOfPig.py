import random
player = 0
total = 0

def roll():
    global total
    dice = random.randint(1,6)
    print("You rolled:", dice)
    if dice == 1:
        total = 0
        print("Your score has reset...")
    total = total + dice
    print("Score so far:", total)
    print()

def hold():
    global player
    global total
    player = player + total
    total = 0

def play():
    while player >= 0:
        choice = input("Would you like to roll or hold? (r/h): ")
        if choice == "r":    
            roll()
        elif choice == "h":
            hold()
            print("Your score is:", player)
            print()
        else:
            print("Please try again")
    
play()