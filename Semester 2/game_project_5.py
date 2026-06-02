import tkinter as tk
import random

# ==========
# RETRO PONG
# ==========

WIDTH = 800
HEIGHT = 500

PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100

BALL_SIZE = 15

def player(canvas):
    canvas.create_rectangle(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, 30 + PADDLE_WIDTH, HEIGHT // 2 + PADDLE_HEIGHT // 2, fill = "white")

def enemy(canvas):
    canvas.create_rectangle(WIDTH - 30 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, WIDTH - 30, HEIGHT // 2 + PADDLE_HEIGHT // 2, fill = "white")

def ball(canvas):
    canvas.create_oval(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, WIDTH // 2 + BALL_SIZE // 2, HEIGHT // 2 + BALL_SIZE // 2, fill = "white")

def line(canvas):
    canvas.create_line(WIDTH // 2, 0, WIDTH // 2, HEIGHT, fill = "white", dash = (10, 10))

def game():
    root = tk.Tk()
    root.title("Retro Pong")

    canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = "black")
    canvas.pack()

    player(canvas)
    enemy(canvas)
    line(canvas)
    ball(canvas)

    root.mainloop()

game()