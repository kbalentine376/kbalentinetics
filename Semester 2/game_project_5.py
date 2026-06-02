import tkinter as tk
import random

WIDTH = 800
HEIGHT = 500

PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
BALL_SIZE = 15


class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Retro Pong")

        self.canvas = tk.Canvas(self.root, width = WIDTH, height = HEIGHT, bg = "black")
        self.canvas.pack()

        # center line
        self.canvas.create_line(WIDTH // 2, 0, WIDTH // 2, HEIGHT, fill = "white", dash = (10, 10))

        # paddles
        self.player = self.canvas.create_rectangle(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, 30 + PADDLE_WIDTH, HEIGHT // 2 + PADDLE_HEIGHT // 2, fill = "white")

        self.enemy = self.canvas.create_rectangle(WIDTH - 30 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, WIDTH - 30, HEIGHT // 2 + PADDLE_HEIGHT // 2, fill = "white")

        # ball
        self.ball = self.canvas.create_oval(WIDTH // 2 - BALL_SIZE, HEIGHT // 2 - BALL_SIZE, WIDTH // 2 + BALL_SIZE, HEIGHT // 2 + BALL_SIZE, fill = "white")

        # velocity
        self.dx = 4
        self.dy = 3

        self.update()

        self.root.mainloop()

    def update(self):
        # move ball
        self.canvas.move(self.ball, self.dx, self.dy)

        x1, y1, x2, y2 = self.canvas.coords(self.ball)

        # bounce top/bottom
        if y1 <= 0 or y2 >= HEIGHT:
            self.dy = -self.dy

        # bounce left/right (reset for now)
        if x1 <= 0 or x2 >= WIDTH:
            self.canvas.coords(self.ball, WIDTH // 2 - BALL_SIZE, HEIGHT // 2 - BALL_SIZE, WIDTH // 2 + BALL_SIZE, HEIGHT // 2 + BALL_SIZE)
            self.dx = -self.dx

        # loop
        self.root.after(16, self.update)


Game()