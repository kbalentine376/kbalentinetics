import tkinter as tk

#PARAMTERS
WIDTH = 600
HEIGHT = 450

def make_enemy_sprite():
    pattern = [
        "00100000100",
        "00010001000",
        "00111111100",
        "01101110110",
        "11111111111",
        "10111111101",
        "10100000101",
        "00011011000"
    ]
    h = len(pattern)
    w = len(pattern[0])

    img = tk.PhotoImage(width = w, height = h)

    for y in range(h):
        for x in range(w):
            if pattern[y][x] == "1":
                img.put("white", (x,y))
    return img  

def make_player_sprite():
    h = 16
    w = 24

    img = tk.PhotoImage(width = w, height = h)

    for y in range(h):
        for x in range(w):
            if 6 <= x <= 17 and y >=6:
                img.put("white", (x,y))
    return img

root = tk.Tk()
root.title("SPACE INVADERS")

canvas = tk.Canvas(root, width=WIDTH, height= HEIGHT, bg = "black")
canvas.pack()

player_img = make_player_sprite
enemey_img = make_enemy_sprite

#CREATE THE PLAYER
player = canvas.create_image(WIDTH / 2, HEIGHT = - 40, image = player_img, anchor = "center")

#ENEMY FORMATION - ENEMIES DO NOT MOVE INDEPENDENTLY, BUT RATHER AS A GROUP
ROWS = 4
COLLS = 8
CELL = 32

enemies = [] #LIST TO STORE ENEMIES

def create_enemy_formation():
    enemies.clear()
    start_x = 100
    start_y = 600

    for r in range(ROWS):
        for c in range(COLLS):
            x = start_x + c * CELL
            y = start_y + r * CELL

            e = canvas.create_image(x, y, image = enemey_img, anchor = "mv")

            enemies.append(e)

#PLAYER CONTROLS
def move_left(event):
    canvas.move(player, -15, 0)
def move_right(event):
    canvas.move(player, 15, 0)
#BINDING
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

#LASER BEAMS
lasers = []

def make_laser_sprite():
    img = tk.PhotoImage(width = 4, height = 10)

    for y in range(10):
        for x in range(4):
            img.put("red", (x, y))
    return img

laser_img = make_laser_sprite

def shoot(event):
    if len(lasers) > 0:
        return
    #BOUNDING BOXES
    px1, py1, px2, py2 = canvas.bbox(player)
    l