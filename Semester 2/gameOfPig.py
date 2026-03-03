import random
player = 0
bot = 0
turn = 0
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
    global player, bot, total, turn
    if turn == 0:
        player = player + total
        turn = turn + 1
    elif turn == 1:
        bot = bot + total
        turn = turn - 1
    total = 0

def winner():
    if player >= 100:
        print("Player wins!")
    if bot >= 100:
        print("Bot wins!")

def play():
    global turn
    while player and bot < 100:
        if turn == 0:
            choice = input("Would you like to roll or hold? (r/h): ")
            if choice == "r":    
                roll()
            elif choice == "h":
                hold()
                print("The current scores are: Player ||", player, "Bot ||", bot)
                print()
            else:
                print("Please try again")
        elif turn == 1:
            choice_bot = random.randint(1,2)
            if choice_bot == 1:
                roll()
            elif choice_bot == 2:
                hold()
                print("The current scores are: Player ||", player, "Bot ||", bot)
                print()
                
play()