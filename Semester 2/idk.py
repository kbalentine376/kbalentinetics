import tkinter as tk
import random

#DECLARE SOME CONSTANTS
WIDTH = 400
HEIGHT = WIDTH * .75
PLAYER_SIZE = 30
ENEMY_SIZE = 20

#BUILD OUR WINDOW
root = tk.Tk()
root.title("Avoid The Blocks!")

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = "black" )
canvas.pack()

#MAKE THE PLAYER
player = canvas.create_rectangle(180, 250, 180 + PLAYER_SIZE, 250 + PLAYER_SIZE, fill = "magenta")

#PLAYER SCORE
score_show = tk.Label(root, text = "Score " + )

#MAKE A LIST TO HOLD ENEMIES
enemies = []

#MAKE AN ALIVE TOOL
alive = True

#MOVEMENT FUNCTIONS
def move_left(event):
    canvas.move(player, - 20, 0)

def move_right(event):
    canvas.move(player, + 20, 0)

#BINDING BUTTONS
root.bind("a", move_left)
root.bind("d", move_right)

#BAD GUYS
def spawn_enemy():
    x = random.randint(0, WIDTH - ENEMY_SIZE)
    enemy = canvas.create_rectangle(x, 0, x + ENEMY_SIZE, ENEMY_SIZE, fill = "cyan")
    enemies.append(enemy)

#RUN GAME
def run_game():
    global alive
    
    if not alive:
        canvas.create_text(WIDTH // 2, HEIGHT // 2, text = "GAME OVER", fill = "white", font = ("Arial", 24))
        return
    
    if random.randint(1, 20) == 1:
        spawn_enemy()
    
    for enemy in enemies:
        canvas.move(enemy, 0, 10)

        if canvas.bbox(enemy) and canvas.bbox(player):
            ex1, ey1, ex2, ey2 = canvas.bbox(enemy)
            px1, py1, px2, py2 = canvas.bbox(player)

            if ex1 < px2 and ex2 > px1 and ey1 < py2 and ey2 > py1:
                alive = False

    root.after(50, run_game)


run_game()
root.mainloop()