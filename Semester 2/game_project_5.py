import tkinter as tk
import random

# ==========
# RETRO PONG
# ==========

def player(canvas):
    canvas.create_rectangle(30, 500 // 2 - 50, 30 + 10, 500 // 2 + 50, fill="white")

def enemy(canvas):
    canvas.create_rectangle(800 - 40, 500 // 2 - 50, 800 - 30, 500 // 2 + 50, fill="white")

def ball(canvas):
    canvas.create_oval(800 // 2 - 15, 500 // 2 - 15, 800 // 2 + 15, 500 // 2 + 15, fill="white")

def line(canvas):
    canvas.create_line(400, 0, 400, 500, fill="white", dash=(10, 10))

def game():
    root = tk.Tk()
    root.title("Retro Pong")

    canvas = tk.Canvas(root, width=800, height=500, bg="black")
    canvas.pack()

    player(canvas)
    enemy(canvas)
    line(canvas)
    ball(canvas)

    root.mainloop()

game()